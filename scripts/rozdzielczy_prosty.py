import csv
from tkinter import CENTER, NO, messagebox

headers = []
data = {}


class RozdzielczyProsty:
    def __init__(self, headers, data, type):
        self.headers = headers
        self.data = data
        self.type = type


# TODO Zapytac uzytkownika o naglowki, jesli plik nie posiada, dodac mozliwosc dodania w programie
def open_file(path, type):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        row_index = 1
        for row in csv_reader:
            if row_index == 1:
                headers = row
            else:
                try:
                    if("," in row[0] or "," in row[1]):
                        data[float(row[0].replace(',', '.'))] = float(
                            row[1].replace(',', '.'))
                    else:
                        data[float(row[0])] = float(row[1])
                except ValueError:
                    res = messagebox.askyesno(title="Blad przy importowaniu danych!",
                                        message=f'Wystapil blad w wierszu nr {row_index}:\n{row[0]}; {row[1]}\nPoprawny format:\nx; y\nCzy chcesz zaimportowac dane bez tego wiersza?')
                    if res==False:
                        return RozdzielczyProsty(headers, data, type)       
            row_index += 1
    return RozdzielczyProsty(headers, data, type)


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
        table.insert(parent='', index='end', iid=index, text='',
                     values=(index + 1, key, data_object.data[key]))
        index += 1
