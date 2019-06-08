import tkinter as tk 

class RootWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__(self)
        self.controller = controller
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    def init_frames(self, frames):
        frames = {}
        for klass in frames:
            frame = klass(parent=container, controller=self.controller)
            name  = klass.__name__ 
            frames[name] = frame 
            
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        return frames 
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.controller.frames[name]
        frame.tkraise()
        return frame 
