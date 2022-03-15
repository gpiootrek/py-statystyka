from pydoc import text
import tkinter as tk
from tkinter import NORMAL, DISABLED, filedialog, font, Tk
import tkinter.font as TkFont
from scripts import prosty, przedzialowy, szereg

# init window
root = tk.Tk()
# root.geometry("600x400")
root.wm_resizable(width=False, height=False)

# fonts
defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Candara",size=18, weight=font.NORMAL)
btnFont = font.Font(weight=font.BOLD)

# handle file upload
def UploadFile(event=None):
    filePath = filedialog.askopenfilename()
    print(dataType.get())
    # TODO if sprawdzający który typ pliku został wybrany i wywołanie funkcji obsługującej import tego typu pliku (przekazanie do funkcji ścieżki pliku)

# handle user click on typeInput btns - activate import btn
def activateImport(event=None):
    print(dataType.get())
    global fileInput
    fileInput['state'] = NORMAL

tk.Label(root, text="Wybierz typ danych do zaimportowania:").grid(row=1, column=1, columnspan=2, sticky=tk.W, padx=2, pady=4)

dataType = tk.Variable()
# initialize type inputs
typeInput1 = tk.Radiobutton(root, text='Szereg prosty', variable=dataType,
                            value="SZEREG_PROSTY", command=activateImport)
typeInput1.grid(row=2, column=1, sticky=tk.W, pady=4)

typeInput2 = tk.Radiobutton(root, text='Szereg rozdzielczy prosty',
                            variable=dataType, value="ROZDZIELCZY_PROSTY", command=activateImport)
typeInput2.grid(row=3, column=1, sticky=tk.W, pady=4)

typeInput3 = tk.Radiobutton(root, text='Szereg rozdzielczy przedzialowy',
                            variable=dataType, value="ROZDZIELCZY_PRZEDZIALOWY", command=activateImport)
typeInput3.grid(row=4, column=1, sticky=tk.W, pady=4)

fileInput = tk.Button(root, text='Open', command=UploadFile, state = DISABLED)
fileInput['font'] = btnFont
fileInput.grid(row=5, column=1, sticky=tk.W, pady=4)

tk.mainloop()