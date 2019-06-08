import tkinter as tk 

class CurrentUser(tk.Frame):
    def __init__(self, parent, controller = None):
        super().__init__(parent)
        self.controller = controller 

    def on_exit_frame_hook(self):
        pass 

    def on_enter_frame_hook(self):
        self.controller.load_current_user()