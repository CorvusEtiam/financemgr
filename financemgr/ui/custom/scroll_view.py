import tkinter as tk 

class ScrollView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._scrollbar = tk.Scrollbar(self, orient = tk.VERTICAL)
        self._scrollbar.pack(fill = tk.Y, side = tk.RIGHT, expand = tk.FALSE)
        self._canvas = tk.Canvas(self, bd = 0, highlightthickness = 0, yscrollcommand = self._scrollbar.set)
        self._canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.TRUE)
        self._scrollbar.config(command = self._canvas.yview)
        self._canvas.xview_moveto(0)
        self._canvas.yview_moveto(0)


        self._interior = tk.Frame(self._canvas)
        self._interior_id = self._canvas.create_window(0, 0, window = self._interior, anchor = tk.NW)

        def _configure_interior(event):
            size = (self._interior.winfo_reqwidth(), self._interior.winfo_reqheight())
            self._canvas.config(scrollregion = "0 0 {} {}".format(*size))
            if self._interior.winfo_reqwidth() != self._canvas.winfo_width():
                self._canvas.config(width = self._interior.winfo_reqwidth())
        self._interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if self._interior.winfo_reqwidth() != self._canvas.winfo_width():
                self._canvas.itemconfigure(self._interior_id, width = self._canvas.winfo_width())

        self._canvas.bind('<Configure>', _configure_canvas)
            
    