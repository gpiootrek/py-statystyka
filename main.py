import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont
from pages import start_page

def darkstyle(root):
    style = ttk.Style(root)
    root.tk.call('source', 'azure dark/azure dark.tcl')
    style.theme_use('azure')
    style.configure("Accentbutton", foreground='white')
    style.configure("Togglebutton", foreground='white')
    return style


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = TkFont.Font(family='arial', size=24)
        self.button_font = TkFont.Font(family='arial', size=16)
        self.stats_font = TkFont.Font(family='arial', size=18)
        self.interpretation_font = TkFont.Font(family='arial', size=14, weight="normal")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        style = darkstyle(self)
        
        self.frames = {}
        
        page_name = start_page.StartPage.__name__
        frame = start_page.StartPage(parent=container, controller=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        
        
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()