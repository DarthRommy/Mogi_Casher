#----------performer.py----------
import glob
import os

import pandas as pd
import PySimpleGUI as sg

from performer.unsunghero import UnsungHero

"""
eventごとの処理を記述した場所。
またmogicasherからInterfaceのwindowが送られてくるので、それを使ってGUIを更新する。
"""
class Performer:
    def __init__(self, window: sg.Window):
        self.window = window
        self.dirname = UnsungHero.parent_dir


    def change_layout(self, event, database, history, tab_list, listbox_list, **kwargs):

        for x in tab_list:
            change_image = f"{x}_image"
            image_loc = f'{self.dirname("images")}/{x}.png'
            image_loc_brg = f'{self.dirname("images")}/{x}_bright.png'

            #選んだやつは白く
            if x == event:
                self.window[x].update(text_color='#ffffff' if x != 'exit' else '#df5656')
                self.window[change_image].update(filename=image_loc_brg)
            
            #それ以外は暗く
            else:
                self.window[x].update(text_color="#5f5f5f")
                self.window[change_image].update(filename=image_loc)
        
        #Homeタブから移動したらInputを無効化        
        self.window['-INPUT-'].update(disabled=True if event != 'home' else False)
        
        #Exitボタンならここで離脱
        if event == 'exit':
            return database, history, listbox_list
        
        #Exitボタン以外の時にタブを切り替える
        for x in tab_list[:3]:
            self.window[x.upper()].update(visible=True if x == event else False)
        
        return database, history, listbox_list

        
    def handle_input(self, values, database, history, listbox_list, **kwargs):
        
        input = values["-INPUT-"]
        
        self.window['-INPUT-'].update('')
        codes = [database[x][1] for x in range(len(database))]

        # "Load"前で初期値をブロック
        if input == "xxxxxxxx":
            return database, history, listbox_list

        try:
            # inputがcodesに含まれない場合↓でエラーを吐く
            tag = database[codes.index(input)][0]
            price = database[codes.index(input)][2]

            history.append(input)

            # GUI更新
            self.window["-RECENT-"].update(f">{tag} {input} ¥{price}")
            self.window["-SUBTOTAL-"].update(f"¥{UnsungHero.calc_subtotal(database, history)}")
            self.window["-PAY-"].update(disabled=False)
            self.window["-CANCEL-"].update(disabled=False)
            self.window["-BROWSE-"].update(disabled=True)
        
        #codesに含まれていないコードは例外処理でブロック
        except ValueError:
            self.window["-RECENT-"].update('>')

        return database, history, listbox_list


    def load_profile(self, database, history, listbox_list, **kwargs):
        try:
            data = sg.popup_get_file(message="", no_window=True, file_types=(("CSV Files", '*.csv'),))
            df = pd.read_csv(data, dtype={0: str, 1: str, 2: int, 3: int})
            df = df.values.tolist()

            #------要素の数が4以外の時------
            for x in df:
                if len(x) > 4 or len(x) < 4:
                    raise ValueError()

            database = df

            #------お馴染みGUIコーナー------
            self.window["-TOTAL-"].update(f"¥{UnsungHero.update_totaly(database)}")
            self.window["-TABLE-"].update(database)
            self.window["-RECENT-"].update(">Succeeded")
            self.window["-INPUT-"].update("")

            #------ついでにlogに保存しましょう------
            UnsungHero.save_profile(database, reference=True)

        except (ValueError, IndexError):
            self.window["-RECENT-"].update(">Invalid Data")              #変なデータだった時

        except FileNotFoundError:
            self.window["-RECENT-"].update(">Canceled")                  #キャンセルしたとき

        return database, history, listbox_list
    

    def cancel_checkout(self, database, history, listbox_list, **kwargs):
        history.clear()
        self.window["-SUBTOTAL-"].update("¥0")
        self.window["-PAY-"].update(disabled=True)
        self.window["-CANCEL-"].update(disabled=True)
        self.window["-RECENT-"].update(">Canceled")

        return database, history, listbox_list


    def checkout(self, database, history, listbox_list, **kwargs):
        for x in database:
            x[3] += history.count(x[1])
        history.clear()

        self.window["-TABLE-"].update(database)
        self.window["-TOTAL-"].update(f"¥{UnsungHero.update_totaly(database)}")
        self.window["-SUBTOTAL-"].update("¥0")
        self.window["-RECENT-"].update(">Thank You")
        self.window["-PAY-"].update(disabled=True)
        self.window["-CANCEL-"].update(disabled=True)

        return database, history, listbox_list

    
    def refresh_analyze(self, database, history, listbox_list, **kwargs):
        reports = glob.glob(f"{self.dirname('report')}/*.csv")
        reports.sort()
        
        overall_list = []
        files_list = listbox_list[:1]

        for f in reports:
            try:
                df = pd.read_csv(f, dtype={0: str, 1: str, 2: int, 3: int})
                df = df.values.tolist()

                for x in df:
                    if len(x) > 4 or len(x) < 4:
                        raise ValueError()

                filename = os.path.splitext(os.path.basename(f))[0]

                files_list.append(filename)
                overall_list.append([filename, f"¥{UnsungHero.update_totaly(df)}"])

            except (ValueError, IndexError):
                pass

        self.window["-ANLIST-"].update(values = files_list)
        self.window["-ANLIST-"].update(set_to_index = 0)
        self.window["-ANTABLE-"].update(overall_list)

        return database, history, listbox_list


    def switch_analyze(self, database, history, values, listbox_list, **kwargs):
        if values["-ANLIST-"] == listbox_list[0]:
            self.refresh_analyze(database, history, listbox_list)

        else:
            try:
                path = f"{UnsungHero.parent_dir('report')}/{values['-ANLIST-']}.csv"
                df = pd.read_csv(path)
                df = df.values.tolist()

                table_list = [[x[0], f"¥{x[2]*x[3]}"] for x in df]
                table_list.append(["TOTAL", f"¥{UnsungHero.update_totaly(df)}"])

            # ファイルが存在しない(Delete Reportした後)場合に発動
            except FileNotFoundError:
                table_list = [["File Not Found", "N/A"]]

            self.window["-ANTABLE-"].update(table_list)

        return database, history, listbox_list