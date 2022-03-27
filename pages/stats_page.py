import tkinter as tk


class StatsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(
            self, text="This is the Stats Page. You will see results here.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("StartPage"))
        button1.pack()
        button2.pack()
