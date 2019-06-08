import tkinter as tk 

from financemgr.db import Session 
from financemgr.model import User 

class SelectUser(tk.Frame):
    DEFAULT_MENU_ITEM = "Select User"
    def __init__(self, parent, controller = None):
        super().__init__(parent)
        self.controller = controller 
        self.title("Select User")
        self._cur_opt = tk.StringVar()
        self._cur_opt.set(SelectUser.DEFAULT_MENU_ITEM)
        self._users = self.controller.get_users()

        if len(self._users) > 0:
            lbl = tk.Label(self, text = "No user found")
            lbl.pack()
            return     
        
        
        self._opt_menu = tk.OptionMenu(
            self, 
            self._cur_opt, 
            SelectUser.DEFAULT_MENU_ITEM,
            *self._users  
        )
        
        self._opt_menu.pack()
        
        self._btn = tk.Button(self, text = "Open", command = self.on_select_cb)
        
        self._btn.pack()
    
    def on_exit_frame_hook(self):
        pass 
        
    def on_enter_frame_hook(self):
        self._cur_opt.set(SelectUser.DEFAULT_MENU_ITEM)

    def on_select_cb(self):
        user = self._cur_opt.get()
        if user != SelectUser.DEFAULT_MENU_ITEM:
            self.controller.open_user_by_name(self._cur_opt.get())

