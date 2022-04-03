import statistics
import tkinter as tk
from tkinter import BOTTOM, CENTER, LEFT, NO, NORMAL, DISABLED, RIGHT, X, Y, Frame, Scrollbar, filedialog, messagebox
from tkinter import ttk
from scripts import szereg_prosty, rozdzielczy_przedzialowy, rozdzielczy_prosty

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.data_object = object
        self.data_type = tk.Variable()

        self.label = tk.Label(
            self, text="Wybierz typ danych do zaimportowania:", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10, padx=24)

        self.type_input1 = tk.Radiobutton(self, text='Szereg prosty', variable=self.data_type,
                                          value="SZEREG_PROSTY", indicator=0, bg="#E8F1F2", selectcolor="#00A8E8", cursor="hand2",
                                          fg="#001219", command=lambda: self.activate_import(self.file_input), font=controller.button_font)
        self.type_input1.pack(side="top", pady=5)

        self.type_input2 = tk.Radiobutton(self, text='Szereg rozdzielczy prosty',
                                          variable=self.data_type, value="ROZDZIELCZY_PROSTY", indicator=0, bg="#E8F1F2",
                                          selectcolor="#00A8E8", cursor="hand2", fg="#001219", command=lambda: self.activate_import(self.file_input), font=controller.button_font)
        self.type_input2.pack(side="top", pady=5)

        self.type_input3 = tk.Radiobutton(self, text='Szereg rozdzielczy przedzialowy',
                                          variable=self.data_type, value="ROZDZIELCZY_PRZEDZIALOWY", indicator=0, bg="#E8F1F2",
                                          selectcolor="#00A8E8", cursor="hand2", fg="#001219", command=lambda: self.activate_import(self.file_input), font=controller.button_font)
        self.type_input3.pack(side="top", pady=5)

        self.file_input = ttk.Button(
            self, text='Wybierz plik', command=lambda: self.upload_file(controller), cursor="hand2", state=DISABLED, style="Accentbutton")
        self.file_input.pack(side="top", pady=10)

    # handle file upload

    def upload_file(self, controller):
        file_path = filedialog.askopenfilename()

        # show warning if no file selected
        if file_path == '':
            messagebox.showerror(
                "Blad", "Nie wskazano pliku. Sprobuj ponownie.")
            return

        if self.data_type.get() == "SZEREG_PROSTY":
            self.data_object = szereg_prosty.open_file(
                file_path, self.data_type.get())
        elif self.data_type.get() == "ROZDZIELCZY_PROSTY":
            self.data_object = rozdzielczy_prosty.open_file(
                file_path, self.data_type.get())
        elif self.data_type.get() == "ROZDZIELCZY_PRZEDZIALOWY":
            self.data_object = rozdzielczy_przedzialowy.open_file(
                file_path, self.data_type.get())

        self.display_stats(controller)

    # handle user click on typeInput btns - activate import btn
    def activate_import(self, inputBtn):
        inputBtn['state'] = NORMAL

    def display_stats(self, controller):
        self.label.configure(text="Wyniki:")
        self.type_input1.destroy()
        self.type_input2.destroy()
        self.type_input3.destroy()
        self.file_input.destroy()

        table_frame = Frame(self)
        table_frame.pack(pady=10)

        data_table = ttk.Treeview(table_frame, selectmode='browse')
        data_table.pack(side=LEFT)

        data_scroll = Scrollbar(table_frame, command=data_table.yview)
        data_scroll.pack(side=RIGHT, fill=Y)

        data_table.configure(yscrollcommand=data_scroll.set)

        if self.data_type.get() == "SZEREG_PROSTY":
            szereg_prosty.SzeregProsty.display_data(data_table, self.data_object)
            szereg_prosty.SzeregProsty.show_stats(self, controller, self.data_object.data)
        elif self.data_type.get() == "ROZDZIELCZY_PROSTY":
            rozdzielczy_prosty.RozdzielczyProsty.display_data(data_table, self.data_object)
            rozdzielczy_prosty.RozdzielczyProsty.show_stats(
                self, controller, self.data_object.data)
        elif self.data_type.get() == "ROZDZIELCZY_PRZEDZIALOWY":
            rozdzielczy_przedzialowy.RozdzielczyPrzedzialowy.display_data(data_table, self.data_object)
            rozdzielczy_przedzialowy.RozdzielczyPrzedzialowy.show_stats(
                self, controller, self.data_object.data)
