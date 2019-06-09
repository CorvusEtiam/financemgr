import tkinter as tk 

class RootWindow(tk.Tk):
    def __init__(self, controller = None, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # super().__init__()
        self.controller = controller
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.geometry('600x400')
        self.container = tk.Frame(self)

        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def init_frames(self, frame_classes):
        frames = {}
        for klass in frame_classes:
            frame = klass(parent=self.container, controller=self.controller)
            name  = klass.__name__ 
            frames[name] = frame 
            
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        return frames 
        
    def show_frame(self, fname):
        '''Show a frame for the given page name'''
        frame = self.controller.frames[fname]
        frame.tkraise()
        return frame 

