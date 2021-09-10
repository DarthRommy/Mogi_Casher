#----------handler.py-----------

from performer.performer import Performer

"""
MogiCasherから送られてくるeventに対応する関数をPerformerから引っ張ってくる。
"""

class Handler:
    def __init__(self, performer: Performer):
        self.performer = performer

        self.functions = {
            "\r": self.performer.handle_input,
            "-BROWSE-": self.performer.load_profile,
            "-CANCEL-": self.performer.cancel_checkout,
            "-PAY-": self.performer.checkout,
            "home": self.performer.change_layout,
            "setting": self.performer.change_layout,
            "exit": self.performer.change_layout,
            "-SETNAME-": self.performer.set_storename
        }

    def handle(self, event, values, tab_list, database, history):
        if callable(event):
            event()

        elif event in self.functions:
            event_func = self.functions[event]
            database, history = event_func(**{"event":event, "values":values, "tab_list":tab_list, "database": database, "history":history})

        else:
            pass
        
        return database, history