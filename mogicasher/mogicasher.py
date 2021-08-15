#-----------mogicasher.py----------

from interface.interface import Interface
from performer.performer import Performer
from performer.handler import Handler
from performer.unsunghero import UnsungHero


"""
めも：
レイアウトと処理を別ファイルで書くことで機能の変更をしやすくしてみた。

mogicasher v1.5
    #---New Features---#
    1. Analyze Tab is now available!!!(1.5.0)
        #Temporarily disabled.(1.5.0.1)
        #Re-activated!(1.5.1)
    2. Changed the method to determine that the code has been loaded at least once!(1.5.0)
    3. Changed the method to get the latest-autosaved files!(1.5.0.0)
    4. Changed Layout!(1.5.0) 
    5. Deleted custom theme...(1.5.1)
"""


class MogiCasher:
    @classmethod
    def main(cls):
        def_color = "lightblue1" #お好みで
        version = "1.5.1"
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
    def control(cls, color, database, version, darkmode=False):

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

            if event in [None, "-RE-", "exit"]:
                if event == "-RE-":
                    restart = True
                break

        interface.window_close()

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
