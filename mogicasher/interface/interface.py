#----------interface.py----------

import PySimpleGUI as sg

from performer.performer import UnsungHero
from interface.style import *

"""
GUIのレイアウトを書いた場所。
"""

class Interface:
    def __init__(self, color, database, app_version, darkmode=False):
        
        #----------Database----------
        self.database = database
        self.history = []
        self.dirname = UnsungHero.system_dir("images")
        

        #----------Theme------------
        self.color = color
        sg.theme(self.color)
        self.version = app_version


        #----------LEFT AREA----------
        #Tab Select Frame

        # 切り替えレイアウトのキー
        self.tab_list = ["home", "setting", "exit"]

        self.select_home = sg.Column(pad=(0,0), layout=[
            [sg.Image(f'{self.dirname}/home_bright.png', enable_events=True, k=f'{self.tab_list[0]}_image', tooltip="メイン画面"),
             sg.Text('Home', **selected_style, k=self.tab_list[0], tooltip="メイン画面")]])
        
        self.select_setting = sg.Column(pad=(0,0), layout=[
            [sg.Image(f'{self.dirname}/setting.png', enable_events=True, k=f'{self.tab_list[1]}_image', tooltip="マニアックな設定ができます"),
             sg.Text('Setting', **select_style, k=self.tab_list[1], tooltip="マニアックな設定ができます")]])

        self.select_exit = sg.Column(pad=(0,(15,0)), layout=[
            [sg.Image(f'{self.dirname}/exit.png', enable_events=True, k=f'{self.tab_list[2]}_image'),
             sg.Text('Exit', **select_style, k=self.tab_list[2])]])

        self.select_air_1 = sg.Column(pad=(5,30), layout=[[sg.Text(' ', font=('sf ui display bold', 12))]])

        self.select_frame = sg.Column(pad=(10,10), layout=[                      #空のレイアウトを使って力技で調整 
                [self.select_air_1],
                [self.select_home],
                [self.select_setting],
                [self.select_exit]
            ])
        

        #----------MIDDLE AREA----------
        #Home Tab
        self.load_frame = sg.Frame("Load Data", font=('sf ui display bold',20), layout=[
            [sg.Button('Browse', font=('sf ui display bold',11), k='-BROWSE-', disabled=self.database != UnsungHero.get_autosave()),
             sg.VerticalSeparator(),
             sg.Text('Find CSV file', font=('sf ui display bold',14), text_color="#5f5f5f", size=(18,1))]
        ])

        self.input_frame = sg.Frame('Input', font=('sf ui display bold',30), layout=[
            [sg.Input('', size=(26,1), disabled=False, font=('consolas',15), k='-INPUT-', focus=True)],
            [sg.Text('>', font=('consolas',15), size=(20,1), k='-RECENT-', text_color="#5f5f5f")],
            [sg.Text('Subtotal:', font=('sf ui display light',15), tooltip="ご精算前の小計になります"),
             sg.Text('¥0', font=('sf ui display light', 15), size=(8,0), key='-SUBTOTAL-')],
            [sg.Button("Cancel", font=("sf ui display bold",13), k="-CANCEL-", disabled=True),
             sg.Button("Check Out", font=("sf ui display bold",13), k="-PAY-", disabled=True)]
        ])

        self.home_frame = [
            [self.load_frame],
            [self.input_frame]
        ]
        
        #Setting Tab
        self.setting_left = sg.Column([
            [sg.Checkbox('Darkmode', default=darkmode, font=('sf ui display bold', 14), k='-DARK-', pad=(5,2), tooltip="みんな大好きダークモードだぜ")],
            ])

        self.setting_right = sg.Column([
            [sg.Text('Custom Font', font=('sf ui display bold',14), k=UnsungHero.font_install, enable_events=True, pad=((5,16),2), text_color="#2d5cff", tooltip="画面がかっこよくなります")],
            [sg.Text("Clear Log", font=("sf ui display bold",14), text_color="#2d5cff", tooltip="自動保存したデータを削除できます", k=UnsungHero.clean_logs, enable_events=True)],
            [sg.Text("Clear Report", font=("sf ui display bold",14), text_color="#2d5cff", tooltip="Analyzeに使うデータを削除できます", k=UnsungHero.clean_reports, enable_events=True)],
            [sg.Text("GitHub", font=("sf ui display bold",14), text_color="#2d5cff", tooltip="ソースコードはここをクリック", k=UnsungHero.view_source, enable_events=True)]
        ])

        self.settings_frame = sg.Frame('Setting', font=('sf ui display bold',30), layout=[
            [sg.Input(font=("メイリオ",12), k="-STORE-", size=(23,1), tooltip="発団名を入れてや", default_text=UnsungHero.read_storename()),
             sg.Button("Submit", font=("sf ui display bold",12), k="-SETNAME-", tooltip="名前を変えたら押してね")],
            [self.setting_left, sg.VerticalSeparator(pad=(10,5)), self.setting_right],
            [sg.Button('Restart', font=('sf ui display bold', 14), k='-RE-', tooltip="変更したら押してね"),
             sg.Text(f"¶ MogiCasher v{self.version}", font=("sf ui display light",12))]
            
            ])

        self.setting_frame = [
            [self.settings_frame]
        ]

        #Switchable Frame
        self.middle_frame = sg.Column([
            [UnsungHero.collapse(self.home_frame, self.tab_list[0].upper(), True)],
            [UnsungHero.collapse(self.setting_frame, self.tab_list[1].upper(), False)]
        ])

        #----------RIGHT AREA----------
        #Database Frame
        self.database_frame = sg.Frame('Database', font=("sf ui display bold",30), layout=[
            [sg.Text("Current sales", font=('sf ui display bold',15))],
            [sg.Table(self.database, **table_style, k="-TABLE-")],
            [sg.Text('Total:', font=('sf ui display bold',18), pad=(5,0), tooltip="チケット売り場での売上"),
             sg.Text(f'¥{UnsungHero.update_totaly(self.database)}', font=('sf ui display bold',19), size=(10,1), key='-TOTAL-')]
        ])

        self.right_frame = sg.Column(pad=((0,10),10), element_justification="C", layout=[
            [self.database_frame]
            ])

        self.window = sg.Window(f"{UnsungHero.read_storename()} ( • q • ) b", layout=[[self.select_frame, self.middle_frame, self.right_frame]], **window_style)
    

    def window_close(self):
        self.window.close()
