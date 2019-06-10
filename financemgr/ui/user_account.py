
import tkinter as tk 
from . import StackFrame

class CurrentUser(StackFrame):
    def __init__(self, parent, controller = None):
        super().__init__(parent, controller)
        user_name_text = tk.Label(self, text = "User: ", width = 20)
        
        self._user_name = tk.Label(self, text = "", width = 20)
        
        #user_name_text.grid(row = 0, column = 0)
        #self._user_name.grid(row = 0, column = 1)

        self._edit_user = tk.Button(self, text = "Edit User", command = self.on_edit_user) 
        
        self._rem_user  = tk.Button(self, text = "Remove User", command = self.on_remove_user) 

    def on_exit_frame_hook(self):
        pass 

    def on_enter_frame_hook(self):
        user = self.controller.current_user 
        self._user_name.config(text = user.name)

    def on_edit_user(self):
        pass 
    def on_remove_user(self):
        pass 