import tkinter as tk
from tkinter import NORMAL, DISABLED, filedialog, messagebox
from scripts import szereg_prosty, rozdzielczy_przedzialowy, rozdzielczy_prosty

data_object = object

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        data_type = tk.Variable()

        label = tk.Label(
            self, text="Wybierz typ danych do zaimportowania:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        typeInput1 = tk.Radiobutton(self, text='Szereg prosty', variable=data_type,
                                    value="SZEREG_PROSTY", indicator=0, bg="#E8F1F2", selectcolor="#90be6d", cursor="hand2",
                                    fg="#001219", command=lambda: self.activate_import(file_input))
        typeInput1.pack(side="top", pady=5)

        typeInput2 = tk.Radiobutton(self, text='Szereg rozdzielczy prosty',
                                    variable=data_type, value="ROZDZIELCZY_PROSTY", indicator=0, bg="#E8F1F2",
                                    selectcolor="#90be6d", cursor="hand2", fg="#001219", command=lambda: self.activate_import(file_input))
        typeInput2.pack(side="top", pady=5)

        typeInput3 = tk.Radiobutton(self, text='Szereg rozdzielczy przedzialowy',
                                    variable=data_type, value="ROZDZIELCZY_PRZEDZIALOWY", indicator=0, bg="#E8F1F2",
                                    selectcolor="#90be6d", cursor="hand2", fg="#001219", command=lambda: self.activate_import(file_input))
        typeInput3.pack(side="top", pady=5)

        file_input = tk.Button(
            self, text='Wybierz plik', command=lambda: self.upload_file(data_type), cursor="hand2", state=DISABLED)
        file_input.pack(side="top", pady=10)


    # handle file upload
    def upload_file(self, data_type):
        file_path = filedialog.askopenfilename()

        # show warning if no file selected
        if file_path == '':
            messagebox.showerror("Blad", "Nie wskazano pliku. Sprobuj ponownie.")
            return
        
        global data_object

        if data_type.get() == "SZEREG_PROSTY":
            data_object = szereg_prosty.open_file(file_path)
        elif data_type.get() == "ROZDZIELCZY_PROSTY":
            data_object = rozdzielczy_prosty.open_file(file_path)
        elif data_type.get() == "ROZDZIELCZY_PRZEDZIALOWY":
            data_object = rozdzielczy_przedzialowy.open_file(file_path)
        
        self.controller.show_frame("StatsPage")
        


    # handle user click on typeInput btns - activate import btn
    def activate_import(self, inputBtn):
        inputBtn['state'] = NORMAL
