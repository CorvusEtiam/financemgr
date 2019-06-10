import tkinter as tk 

from financemgr.db import Session 
from financemgr.model import User 
from . import StackFrame 

class SelectUser(StackFrame):
    DEFAULT_MENU_ITEM = "Select User"
    def __init__(self, parent, controller = None):
        super().__init__(parent, controller)
        self._cur_opt = tk.StringVar()
        self._users = self.controller.get_users()

        if not self._users:
            lbl = tk.Label(self, text = "No user found")
            lbl.pack()
            return     
        
        
        lbl = tk.Label(self, text = "Please select user to be displayed or add new user")
        lbl.pack()        
        
        self._cur_opt.set(self._users[0])
        
        self._opt_menu = tk.OptionMenu(
            self, 
            self._cur_opt,
            *self._users 
        )
        
        self._opt_menu.pack()
        
        self._btn = tk.Button(self, text = "Open", command = self.on_read_cb)
        
        self._btn.pack()

        self._create_btn = tk.Button(self, text = "Create New User", command = self.on_create_click)
        
        self._create_btn.pack()

        self._create_btn = tk.Button(self, text = "Edit User", command = self.on_update_click)
        
        self._create_btn.pack()


        self._create_btn = tk.Button(self, text = "Remove User", command = self.on_delete_click)
        
        self._create_btn.pack()
    
    def on_exit_frame_hook(self):
        pass 
        
    def on_enter_frame_hook(self):
        self._users = self.controller.get_users()
        self._cur_opt.set(self._users[0])
        menu = self._opt_menu["menu"]
        menu.delete(0, "end")
        for user in self._users:
            menu.add_command(label = user.name, command  = tk._setit(self._cur_opt, user))

    def on_read_cb(self):
        user = self._cur_opt.get()
        if user != SelectUser.DEFAULT_MENU_ITEM:
            user_ = self.controller.get_user_by_name(self._cur_opt.get())
            if user_ is not None:
                self.controller.current_user = user_ 
                self.controller.change_ui("CurrentUser")
            else:
                raise Exception(f"Unknown User : {user}")
            
    def on_create_click(self):
        self.controller.create_user()

    def on_update_click(self):
        self.controller.current_user = self._cur_opt.get()
        self.controller.update_user()
    
    def on_delete_click(self):
        self.controller.current_user = self._cur_opt.get()
        self.controller.delete_user()
    