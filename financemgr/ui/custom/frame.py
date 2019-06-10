import tkinter as tk 

class StackFrame(tk.Frame):
	def __init__(self, master, controller, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.controller = controller

	def on_exit_frame_hook(self):
		raise NotImplementedError("No default implementation for exit frame hook")
    
	def on_enter_frame_hook(self):
		raise NotImplementedError("No default implementation for enter frame hook")
	
