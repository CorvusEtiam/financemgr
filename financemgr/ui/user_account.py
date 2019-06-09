
import tkinter as tk 
from .frame import StackFrame

class CurrentUser(StackFrame):
    def __init__(self, parent, controller = None):
        super().__init__(parent, controller)

    def on_exit_frame_hook(self):
        pass 

    def on_enter_frame_hook(self):
        self.controller.load_current_user()