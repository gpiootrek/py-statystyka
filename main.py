import tkinter as tk
import tkinter.font as TkFont
from pages import start_page

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = TkFont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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