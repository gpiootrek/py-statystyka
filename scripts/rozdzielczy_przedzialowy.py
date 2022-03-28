import csv
from tkinter import CENTER, NO

headers = []
data = {}

class RozdzielczyPrzedzialowy:
    def __init__(self, headers, data, type):
        self.headers = headers
        self.data = data

def open_file(path, type):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        row_index = 1
        for row in csv_reader:
            if row_index == 1:
                headers = row
            else:
                a, b = row[0].split('-')
                data[(float(a),float(b))] = float(row[1])
            row_index+=1
    return RozdzielczyPrzedzialowy(headers, data, type)
    
def display_data(table, data_object):
    table['columns'] = ('lp', data_object.headers[0], data_object.headers[1])

    table.column("#0", width=0,  stretch=NO)
    table.column("lp", anchor=CENTER, width=40)
    table.column(data_object.headers[0], anchor=CENTER, width=80)
    table.column(data_object.headers[1], anchor=CENTER, width=80)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("lp", text="L.p.", anchor=CENTER)
    table.heading(data_object.headers[0],
                  text=data_object.headers[0], anchor=CENTER)
    table.heading(data_object.headers[1],
                  text=data_object.headers[1], anchor=CENTER)

    index = 0

    for key in data_object.data:
        min, max = key
        table.insert(parent='', index='end', iid=index, text='',
                     values=(index + 1, f'{min} - {max}', data_object.data[key]))
        index += 1
