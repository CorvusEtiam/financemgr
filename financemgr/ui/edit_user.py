import tkinter as tk 
from tkinter import ttk 
from .frame import StackFrame 


class EditUser(StackFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        lbl = tk.Label(self, text = "Name: ")
        self._user_name = tk.StringVar()
        self._text_edit = ttk.Entry(self, textvariable=self._user_name)
        self._account_count_lbl = tk.Label(self, text = "Number of accounts: 0")
        self._account_box = tk.Listbox(self)        
          
        button_box = tk.Frame(self)
        
        self._account_add  = tk.Button(button_box, text = "Add Account", command = self.on_add_click)
        self._account_add.pack(side = tk.RIGHT)
        
        self._account_del  = tk.Button(button_box, text = "Remove Account", command = self.on_del_click)
        self._account_del.pack(side = tk.RIGHT)
        
        self._account_upd  = tk.Button(button_box, text = "Edit Account", command = self.on_upd_click)
        self._account_upd.pack(side = tk.RIGHT)
        
        self._account_view = tk.Button(button_box, text = "Show Account", command = self.on_view_click)
        self._account_view.pack(side = tk.RIGHT)

        button_box.pack()

    def on_exit_frame_hook(self):
        pass
    
    def on_enter_frame_hook(self):
        self._user_name.set(self.controller.current_user.name)
        accounts = self.controller.current_user.accounts
        self._account_count_lbl.config(text = "Number of account: {}".format(len(accounts)))
        self._account_box.delete(1, self._account_box.size())
        for i, account in enumerate(accounts):
            self._account_box.insert(i, account.name)

    def on_add_click(self):
        pass 
    def on_del_click(self):
        pass 
    def on_upd_click(self):
        pass 
    def on_view_click(self):
        pass 
    