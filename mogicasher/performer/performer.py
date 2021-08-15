#----------performer.py----------
import os

import pandas as pd
import PySimpleGUI as sg
from pathlib import Path
from performer.unsunghero import UnsungHero

"""
eventごとの処理を記述した場所。
またmogicasherからInterfaceのwindowが送られてくるので、それを使ってGUIを更新する。
"""
class Performer:
    def __init__(self, window: sg.Window):
        self.window = window
        self.dirname = Path(Path(__file__).parent).parent


    def change_layout(self, event, database, history, tab_list, **kwargs):

        for x in tab_list:
            change_image = f"{x}_image"
            image_loc = f'{self.dirname}/system/images/{x}.png'
            image_loc_brg = f'{self.dirname}/system/images/{x}_bright.png'

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
            return database, history
        
        #Exitボタン以外の時にタブを切り替える
        for x in tab_list[:3]:
            self.window[x.upper()].update(visible=True if x == event else False)
        
        return database, history

        
    def handle_input(self, values, database, history, **kwargs):
        
        input = values["-INPUT-"]
        
        self.window['-INPUT-'].update('')
        codes = [database[x][1] for x in range(len(database))]

        # "Load"前で初期値をブロック
        if input == "xxxxxxxx":
            return database, history

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

        return database, history


    def load_profile(self, database, history, **kwargs):
        try:
            data = sg.popup_get_file(message="", no_window=True, file_types=(("CSV Files", '*profile*.csv'),))
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

        return database, history
    

    def cancel_checkout(self, database, history, **kwargs):
        history.clear()
        self.window["-SUBTOTAL-"].update("¥0")
        self.window["-PAY-"].update(disabled=True)
        self.window["-CANCEL-"].update(disabled=True)
        self.window["-RECENT-"].update(">Canceled")

        return database, history 


    def checkout(self, database, history, **kwargs):
        for x in database:
            x[3] += history.count(x[1])
        history.clear()

        self.window["-TABLE-"].update(database)
        self.window["-TOTAL-"].update(f"¥{UnsungHero.update_totaly(database)}")
        self.window["-SUBTOTAL-"].update("¥0")
        self.window["-RECENT-"].update(">Thank You")
        self.window["-PAY-"].update(disabled=True)
        self.window["-CANCEL-"].update(disabled=True)

        return database, history
