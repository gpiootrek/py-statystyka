import tkinter as tk
from tkinter import NORMAL, DISABLED, filedialog, font, Tk
import tkinter.font as TkFont

# init window
root = tk.Tk()
# root.geometry("600x400")
root.wm_resizable(width=False, height=False)

# fonts
# default_font = TkFont.nametofont("TkDefaultFont")
# default_font.configure(family="Helvetica", size=24)
# root.option_add("*Font", default_font)

defaultFont = font.nametofont("TkDefaultFont")
  
        # Overriding default-font with custom settings
        # i.e changing font-family, size and weight
defaultFont.configure(family="Fixedsys",
                                   size=19,
                                   weight=font.BOLD)

# fontSm = TkFont.Font(family="Raavi", size=18, weight="normal")
# fontMd = TkFont.Font(family="Raavi", size=24, weight="normal")
# fontLg = TkFont.Font(family="Raavi", size=36, weight="bold")

# handle file upload
def UploadFile(event=None):
    path = filedialog.askopenfilename()
    importedFile = open(path, 'r')
    for line in importedFile:
        print(line[:-1:])
        
    

# handle user click on typeInput btns - activate import btn
def activateImport(event=None):
    print(var.get())
    global fileInput
    fileInput['state'] = NORMAL

var = tk.Variable()

tk.Label(root, text="Wybierz importowany typ danych:").grid(row=1, column=1, columnspan=2, sticky=tk.W, padx=2, pady=4)

# initialize type inputs and deselect 2 of 3 
typeInput1 = tk.Radiobutton(root, text='Szereg prosty', variable=var,
                            value="SZEREG_PROSTY", command=activateImport)
typeInput1.grid(row=2, column=1, sticky=tk.W, pady=4)

typeInput2 = tk.Radiobutton(root, text='Szereg rozdzielczy prosty',
                            variable=var, value="ROZDZIELCZY_PROSTY", command=activateImport)
typeInput2.grid(row=2, column=2, sticky=tk.W, pady=4)
typeInput2.deselect()

typeInput3 = tk.Radiobutton(root, text='Szereg rozdzielczy przedzialowy',
                            variable=var, value="ROZDZIELCZY_PRZEDZIALOWY", command=activateImport)
typeInput3.grid(row=2, column=3, sticky=tk.W, pady=4)
typeInput3.deselect()

fileInput = tk.Button(root, text='Open', command=UploadFile, state = DISABLED)
fileInput.grid(row=4, column=1, sticky=tk.W, pady=4)

tk.mainloop()
