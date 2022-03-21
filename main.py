from pydoc import text
import tkinter as tk
from tkinter import NORMAL, DISABLED, filedialog, font, Tk
import tkinter.font as TkFont
from scripts import rozdzielczy_prosty, rozdzielczy_przedzialowy, szereg_prosty

# ???
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# initialize window
root = tk.Tk()
root.geometry("600x400")
root.wm_resizable(width=False, height=False)
root.configure(background="#0a0908")

# fonts
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Candara",size=18, weight=font.NORMAL)
btn_font = font.Font(weight=font.BOLD)
warn_font = font.Font(size=12, weight=font.BOLD)

# widgets
warning = tk.Label(root, text="Nie wybrano pliku. Sprobuj ponownie.", bg="#0a0908", fg="#ba181b")

# handle file upload
def upload_file(event=None):
    file_path = filedialog.askopenfilename()
    # show warning if no file selected
    if(file_path == ''):
        warning['font'] = warn_font
        warning.grid(row=6, column=1, sticky=tk.W, pady=8, padx=8)
        return
    else:
        warning.destroy()

    if (data_type.get() == "SZEREG_PROSTY"):
        szereg_prosty.open_file(file_path)
    elif (data_type.get() == "ROZDZIELCZY_PROSTY"):
        rozdzielczy_prosty.open_file(file_path)
    elif (data_type.get() == "ROZDZIELCZY_PRZEDZIALOWY"):
        rozdzielczy_przedzialowy.open_file(file_path)
        
# handle user click on typeInput btns - activate import btn
def activate_import(event=None):
    global file_input
    file_input['state'] = NORMAL

tk.Label(root, text="Wybierz typ danych do zaimportowania:", bg="#0a0908", fg="#E8F1F2").grid(row=1, column=1, columnspan=2, sticky=tk.W, padx=8, pady=4)

data_type = tk.Variable()
# initialize type inputs
typeInput1 = tk.Radiobutton(root, text='Szereg prosty', variable=data_type,
                            value="SZEREG_PROSTY", indicator = 0, bg="#E8F1F2", selectcolor="#90be6d", cursor="hand2", fg="#001219", command=activate_import)
typeInput1.grid(row=2, column=1, sticky=tk.W, pady=4, padx=8)

typeInput2 = tk.Radiobutton(root, text='Szereg rozdzielczy prosty',
                            variable=data_type, value="ROZDZIELCZY_PROSTY", indicator = 0, bg="#E8F1F2", selectcolor="#90be6d", cursor="hand2", fg="#001219", command=activate_import)
typeInput2.grid(row=3, column=1, sticky=tk.W, pady=4, padx=8)

typeInput3 = tk.Radiobutton(root, text='Szereg rozdzielczy przedzialowy',
                            variable=data_type, value="ROZDZIELCZY_PRZEDZIALOWY", indicator = 0, bg="#E8F1F2", selectcolor="#90be6d", cursor="hand2", fg="#001219", command=activate_import)
typeInput3.grid(row=4, column=1, sticky=tk.W, pady=4, padx=8)

file_input = tk.Button(root, text='Wybierz plik', command=upload_file, cursor="hand2", state = DISABLED)
file_input['font'] = btn_font
file_input.grid(row=5, column=1, sticky=tk.W, pady=8, padx=8)

tk.mainloop()