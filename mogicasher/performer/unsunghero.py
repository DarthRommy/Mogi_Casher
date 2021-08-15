#----------unsunghero.py-----------

import datetime
import glob
import os
import shutil
import subprocess
import webbrowser
from pathlib import Path

import pandas as pd
import PySimpleGUI as sg


class UnsungHero:
    """
    UnsungHero contains various functions that provides multiple features of this software.
    """
    dirname = f"{Path(Path(__file__).parent).parent}/system"

    @classmethod
    def subprocess_args(cls, include_stdout=True):
        """
        About this -> https://github.com/pyinstaller/pyinstaller/wiki/Recipe-subprocess
        """
        # exe化して実行した時に出るエラーを防ぐ。
        # shell=Trueでコマンドラインを開こうとするが、--noconsoleオプションで押さえつけられてエラーが出るらしい。
        # さっぱりわからん

        if hasattr(subprocess, 'STARTUPINFO'):
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            env = os.environ
        else:
            si = None
            env = None

        if include_stdout:
            ret = {'stdout': subprocess.PIPE}
        else:
            ret = {}

        ret.update({'stdin': subprocess.PIPE,
                    'stderr': subprocess.PIPE,
                    'startupinfo': si,
                    'env': env })
        return ret


    @classmethod
    def get_autosave(cls):
        """
        get_autosave imports the latest file from "log" folder.
        :Also being a gatekeeper that allows only the correct data.

        Args:

        Returns:
            [[str or int]]:
                Will be an important list "database" and shown in the window.
                [[f"#{x+1}", "xxxxxxxx", 0, 0] for x in range(5)]: The imported data was incorrect or there was no file in "log" folder.
                Other: The imported data was correct.
        """
        # logフォルダ内のファイル一覧をゲットして作成日時で並べ替える
        path = f"{UnsungHero.dirname}/log/*.csv"
        files = glob.glob(path)
        files.sort(reverse=True, key=lambda x: os.path.getctime(x))

        # 完全にtry節にハマってしまった
        try:
            df = pd.read_csv(files[0], dtype={0: str, 1: str, 2: int, 3: int}, on_bad_lines="error")
            def_database = df.values.tolist()

            # 1行でも要素が4以外ならエラー判定
            for x in def_database:
                if len(x) > 4 or len(x) < 4:
                    raise ValueError()
        
        # エラーが出た場合デフォルトのリストになる
        except (IndexError, ValueError):
            def_database = [[f"#{x+1}", "xxxxxxxx", 0, 0] for x in range(5)]

        return def_database
        

    @classmethod
    def collapse(cls, layout, key, visible):
        """
        collapse adjusts the size of the window to fit the layout.
        About this -> https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-collapsible-sections-visible-invisible-elements
        """
        return sg.pin(sg.Column(layout, key=key, visible=visible))


    @classmethod
    def update_totaly(cls, database):
        """
        update_totaly calculates the current sales from "database" list.
        Used as: window[key].update(f"¥{update_totaly(database)}")

        Args:
            database [[str or int]]:
                The list includes codes, prices and units sold. -> self.database

        Returns:
            int:
                Will be displayed in the window.
        """
        totaly = 0
        for x in database:
            totaly += int(x[2])*int(x[3])
        return totaly

    
    @classmethod
    def calc_subtotal(cls, database, history):
        """
        calc_subtotal calculates the temporary sales from "database" and "history" list.
        Used as: window[key].update(f"¥{update_totaly(database, history)}")

        Args:
            database [[str or int]]:
                The list includes codes, prices and units sold. -> self.database

            history [str]:
                The temporary list of the codes until checkout. -> self.history

        Returns:
            int:
                Will be displayed in the window.
        """
        subtotal = 0
        for x in database:
            subtotal += history.count(x[1])*x[2]
        return subtotal


    @classmethod
    def save_profile(cls, database, reference=False, **kwargs):
        
        path = f"{UnsungHero.dirname}/log"
        if not os.path.exists(path):
            os.mkdir(path)

        # Loadした時の実行なら
        if reference:
            extention = "reference"
        else:
            extention = datetime.datetime.now().strftime("%m%d-%H%M")

        #DataFrameで表形式にする
        headings = ["", "CODE", "PRICE", "UNITS"]
        log_database = pd.DataFrame(database, columns=headings)
        log_database = log_database.set_index(headings[0])

        log_database.to_csv(f"{path}/profile[{extention}].csv")


    @classmethod
    def print_anything(cls, *args):
        """
        print_anything prints variables given in the argument one by one.

        Args:
            *args any:
                Any types of variables

        Returns:

        """
        for x in args:
            print (x)


    #----------インスタンスに関わらない関数----------
    @classmethod
    def clean_logs(cls):
        target = f"{UnsungHero.dirname}/log"
        shutil.rmtree(target)
        os.mkdir(target)


    @classmethod
    def view_source(cls):
        
        link = "https://github.com/DarthRommy/MogiCasher/"
        webbrowser.open(link)


    @classmethod
    def add_profile(cls):

        try:
            file = sg.popup_get_file("", file_types=(("csv", "*profile*.csv"),), no_window=True)

            copy_dir = f"{UnsungHero.dirname}/report"
            if os.path.exists(copy_dir):
                os.mkdir

            shutil.copy(file, copy_dir)

        except FileNotFoundError:
            pass


    @classmethod
    def font_install(cls):
        
        font_files = glob.glob(f"{UnsungHero.dirname}/fonts/*.ttf")
        for x in font_files:
            # exe化した際に起きるエラーを防ぐためにこの形式を使う
            try:
                subprocess.Popen(['start', '', f'{x}'], shell=True, **UnsungHero.subprocess_args(True))
            except (subprocess.CalledProcessError, IndexError, OSError):
                pass
