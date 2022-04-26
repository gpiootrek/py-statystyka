import csv
import tkinter as tk
from tkinter import CENTER, NO, messagebox
from scripts import przedzialowy_stat, labels
headers = []
data = {}


def open_file(path, type):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        row_index = 1
        for row in csv_reader:
            if row_index == 1:
                headers = row
            else:
                try:
                    a, b = row[0].split('-')
                    data[(float(a),float(b))] = float(row[1])
                except ValueError:
                    res = messagebox.askyesno(title="Blad przy importowaniu danych!",
                                        message=f'Wystapil blad w wierszu nr {row_index}:\n{row[0]}; {row[1]}\nPoprawny format:\nx - y; z\nCzy chcesz zaimportowac dane bez tego wiersza?')
                    if res==False:
                        return RozdzielczyPrzedzialowy(headers, data, type)
            row_index+=1
    return RozdzielczyPrzedzialowy(headers, data, type)


class RozdzielczyPrzedzialowy:
    def __init__(self, headers, data, type):
        self.headers = headers
        self.data = data
        
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

    # calc and show stats
    def show_stats(root, controller, data):

        stats = przedzialowy_stat.Statistics(data)
        mean = stats.mean
        stdev = stats.stdev
        interpretations = labels.Labels(stats.kurtoza, stats.wspzm, stats.wspasm)

        mean_label = tk.Label(
            root, text=f"Srednia: {round(mean,2)}", font=controller.stats_font)
        mean_label.pack()

        mean_interpretation = tk.Label(
            root, text=f"Srednia wartosc w badanej próbie wynosi {round(mean,2)}", font=controller.interpretation_font, foreground="#ccc")
        mean_interpretation.pack()

        stdev_label = tk.Label(
            root, text=f"Odchylenie standardowe: {round(stdev,2)}", font=controller.stats_font)
        stdev_label.pack()

        stdev_interpretation = tk.Label(root, text=f"O tyle przecietnie roznia sie obserwacje od sredniej.", font=controller.interpretation_font, foreground="#ccc")
        stdev_interpretation.pack()

        wspzm_label = tk.Label(
            root, text=f"Wspolczynnik zmiennosci: {stats.wspzm}%", font=controller.stats_font)
        wspzm_label.pack()

        wspzm_interpretation = tk.Label(root, text=interpretations.get_wspzm_label(), font=controller.interpretation_font, foreground="#ccc")
        wspzm_interpretation.pack()

        wspasm_label = tk.Label(
            root, text=f"Wspolczynnik asymetrii: {stats.wspasm}", font=controller.stats_font)
        wspasm_label.pack()

        wspasm_interpretation = tk.Label(root, text=interpretations.get_wspasm_label(), font=controller.interpretation_font, foreground="#ccc")
        wspasm_interpretation.pack()

        kurtoza_label = tk.Label(
            root, text=f"Kurtoza: {stats.kurtoza}", font=controller.stats_font)
        kurtoza_label.pack()

        kurtoza_interpretation = tk.Label(root, text=interpretations.get_kurtoza_label(), font=controller.interpretation_font, foreground="#ccc")
        kurtoza_interpretation.pack()
