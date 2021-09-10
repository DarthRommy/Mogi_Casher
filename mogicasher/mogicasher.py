#-----------mogicasher.py----------

from interface.interface import Interface
from performer.performer import Performer
from performer.handler import Handler
from performer.unsunghero import UnsungHero

"""
めも：
レイアウトと処理を別ファイルで書くことで機能の変更をしやすくしてみた。
v1.5.3(beta)
    1. 発団名を登録する機能を追加。⇒保存データの判別用
    2. Analyzeは一旦捨てる。
"""

class MogiCasher:
    @classmethod
    def main(cls):
        def_color = "lightblue1" #お好みで
        version = "1.5.3β"
        def_database = UnsungHero.get_autosave()

        argsdict = {"color":def_color, "database":def_database, "version":version}

        while True:

            argsdict = MogiCasher.control(**argsdict)
            if not argsdict["restart"]:
                break


            if argsdict["darkmode"]:
                color = 'darkgrey11'

            else:
                color = def_color

            del argsdict["restart"]

            argsdict["version"] = version
            argsdict["color"] = color


    @classmethod
    def control(cls, color: str, database: list, version: str, darkmode=False):

        interface = Interface(color, database, version, darkmode)
        updater = Performer(window=interface.window)
        handler = Handler(updater)

        database = interface.database
        history = interface.history
        tab_list = interface.tab_list
        
        restart = False
        darkmode = False

        while True:
            event, values = interface.window.read()

            try:
                event = event.replace("_image", "")
            except AttributeError:
                pass

            database, history = handler.handle(event, values, tab_list, database, history)

            darkmode = values["-DARK-"]

            if event in [None, "-RE-", "exit", "-SETNAME-"]:
                if event in ["-RE-", "-SETNAME-"]:
                    restart = True
                break

            interface.window["-INPUT-"].set_focus()

        interface.window_close()

        #-----database != get_autosave()について-----
            # get_autosaveはlogフォルダ内の最新のCSVを読み込む関数。
            # 最新のCSVが現在のdatabaseと等しい=新しい売り上げはないといえる。
            # そうでない場合にdatabaseを保存する。

        if not restart and database != UnsungHero.get_autosave():
            UnsungHero.save_profile(database)

        returnsdict = {
            "restart": restart,
            "darkmode": darkmode,
            "database": database,
        }

        return returnsdict

    
if __name__ == "__main__":
    MogiCasher().main()
