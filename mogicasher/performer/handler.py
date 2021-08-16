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
            "analyze": self.performer.change_layout,
            "setting": self.performer.change_layout,
            "exit": self.performer.change_layout,
            "-REFRESH-": self.performer.refresh_analyze,
            "-ANLIST-": self.performer.switch_analyze,
        }

    def handle(self, event, values, tab_list, database, history, listbox_list):
        if callable(event):
            event()
            return database, history, listbox_list

        elif event not in self.functions:
            return database, history, listbox_list
        
        event_func = self.functions[event]
        database, history, listbox_list = event_func(**{"event":event, "values":values, "tab_list":tab_list, "database": database, "history":history, "listbox_list": listbox_list})
        
        return database, history, listbox_list