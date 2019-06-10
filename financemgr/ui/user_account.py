
import tkinter as tk 
from financemgr.ui.custom.frame import StackFrame
from tkinter.messagebox import askokcancel


class CurrentUser(StackFrame):
    def __init__(self, master, controller = None):
        super().__init__(master, controller)
        lbl_frame = tk.Frame(self)
        user_name_text = tk.Label(lbl_frame, text = "User: ", width = 20)
        user_name_text.grid(row = 0, column = 0)
        self._user_name = tk.Label(lbl_frame, text = "", width = 20)
        self._user_name.grid(row = 0, column = 1)
        
        lbl_frame.pack(side = tk.TOP)
        #user_name_text.grid(row = 0, column = 0)
        #self._user_name.grid(row = 0, column = 1)
        btn_frame = tk.Frame(self)
        btn_frame.pack(side = tk.BOTTOM, fill = tk.BOTH)
        edit_user = tk.Button(btn_frame, text = "Edit User", command = self.on_edit_user) 
        edit_user.pack(side = tk.LEFT)
        rem_user  = tk.Button(btn_frame, text = "Remove User", command = self.on_remove_user) 
        rem_user.pack(side = tk.LEFT)

        go_back = tk.Button(btn_frame, text=  "Go Back", command = self.on_select_user)
        go_back.pack(side = tk.RIGHT)        

    def on_exit_frame_hook(self):
        pass 
    
    def on_enter_frame_hook(self):
        user = self.controller.current_user 
        self._user_name.config(text = user.name)

    def on_select_user(self):
        self.controller.current_user = None 
        self.controller.change_ui('SelectUser')

    def on_edit_user(self):
        self.controller.change_ui("EditUser")

    def on_remove_user(self):
        POPUP_MESSAGE = "Do you want to remove user: {}".format(self.controller.current_user.name)
        choice = askokcancel(title = "Remove User?", message = POPUP_MESSAGE)
        if choice == True:
            self.controller.remove_user(self.controller.current_user)
        