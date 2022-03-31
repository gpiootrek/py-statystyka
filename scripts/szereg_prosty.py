import csv
import statistics
from tkinter import CENTER, NO, messagebox
import tkinter as tk

data = []


class SzeregProsty:
    def __init__(self, data, type):
        self.headers = ["", ""]
        self.data = data


def open_file(path, type):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        row_index = 0
        for row in csv_reader:
            try:
                data.append(float(row[0].replace(',', '.')))
            except (ValueError):
                res = messagebox.askyesno(title="Blad przy importowaniu danych!",
                                       message=f'Wystapil blad w wierszu nr {row_index}:\n{row[0]}\nCzy chcesz zaimportowac dane bez tego wiersza?')
                if res==False:
                    return SzeregProsty(data, type)                    
            row_index += 1
    data.sort()
    return SzeregProsty(data, type)


def display_data(table, data_object):
    table['columns'] = ('lp', 'wartosc')

    table.column("#0", width=0,  stretch=NO)
    table.column("lp", anchor=CENTER, width=40)
    table.column("wartosc", anchor=CENTER, width=80)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("lp", text="L.p.", anchor=CENTER)
    table.heading("wartosc", text="Wartosc", anchor=CENTER)

    index = 0

    for row in data_object.data:
        table.insert(parent='', index='end', iid=index, text='',
                     values=(index + 1, row))
        index += 1

def show_stats(root, controller, data):
    mean_label = tk.Label(
        root, text=f"Srednia: {round(statistics.mean(data),2)}", font=controller.stats_font)
    mean_label.pack()
    median_label = tk.Label(
        root, text=f"Mediana: {round(statistics.median(data),2)}", font=controller.stats_font)
    median_label.pack()
    stdev_label = tk.Label(
        root, text=f"Odchylenie standardowe: {round(statistics.stdev(data),2)}", font=controller.stats_font)
    stdev_label.pack()