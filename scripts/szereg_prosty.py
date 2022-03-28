import csv
from tkinter import CENTER, NO

data = []

class SzeregProsty:
    def __init__(self, data, type):
        self.headers = ["", ""]
        self.data = data

def open_file(path, type):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            data.append(float(row[0].replace(',', '.')))
    return SzeregProsty(data, type)

def display_data(table, data_object):
        table['columns'] = ('lp', 'wartosc')
        
        table.column("#0", width=0,  stretch=NO)
        table.column("lp", anchor=CENTER, width=40)
        table.column("wartosc", anchor=CENTER, width=80)
        
        table.heading("#0", text="",anchor=CENTER)
        table.heading("lp", text="L.p.", anchor=CENTER)
        table.heading("wartosc", text="Wartosc", anchor=CENTER)

        index = 0
        
        for row in data_object.data:
            table.insert(parent='', index='end', iid=index, text='',
                            values=(index + 1, row))
            index += 1