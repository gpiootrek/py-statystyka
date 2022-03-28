import tkinter as tk
from pages import start_page

class StatsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self, text="This is the Stats Page. You will see results here.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Wróć do menu", cursor="hand2",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        self.calc(start_page.data_object)
        
    def calc(self, data):
        print(data)
