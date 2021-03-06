import csv
from math import sqrt
import statistics
from tkinter import CENTER, LEFT, NO, messagebox
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
from scripts import szereg_stat, labels
data = []


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
                if res == False:
                    return SzeregProsty(data, type)
            row_index += 1
    data.sort()
    return SzeregProsty(data, type)


class SzeregProsty:
    def __init__(self, data, type):
        self.headers = ["", ""]
        self.data = data

    # display sorted data in treeview
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

    # calc and show stats
    def show_stats(root, controller, data):

        stdev = statistics.stdev(data)
        mean = statistics.mean(data)
        stats = szereg_stat.Statistics(data, stdev, mean)
        
        interpretations = labels.Labels(stats.kurtoza, stats.wspzm, stats.wspasm)

        mean_label = tk.Label(
            root, text=f"Srednia: {round(mean,2)}", font=controller.stats_font)
        mean_label.pack()

        mean_interpretation = tk.Label(
            root, text=f"Srednia wartosc w badanej pr??bie wynosi {round(mean,2)}", font=controller.interpretation_font, foreground="#ccc")
        mean_interpretation.pack()

        median_label = tk.Label(
            root, text=f"Mediana: {round(statistics.median(data),2)}", font=controller.stats_font)
        median_label.pack()

        median_interpretation = tk.Label(
            root, text=f"Liczba {round(statistics.median(data),2)} dzieli obserwacje na 2 rowne co do ilosci grupy.", font=controller.interpretation_font, foreground="#ccc")
        median_interpretation.pack()

        stdev_label = tk.Label(
            root, text=f"Odchylenie standardowe: {round(stdev,2)}", font=controller.stats_font)
        stdev_label.pack()

        stdev_interpretation = tk.Label(root, text=f"O tyle przecietnie roznia sie obserwacje od sredniej.", font=controller.interpretation_font, foreground="#ccc")
        stdev_interpretation.pack()

        range_label = tk.Label(
            root, text=f"Rozstep: {round(data[-1] - data[0],2)}", font=controller.stats_font)
        range_label.pack()

        range_interpretation = tk.Label(root, text=f"Jest to roznica miedzy wartoscia max a min.", font=controller.interpretation_font, foreground="#ccc")
        range_interpretation.pack()

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

        hist_label = tk.Label(
            root, text="Histogram:", font=controller.stats_font)
        hist_label.pack()

        createHist(root, data)


# create and display histogram
def createHist(root, data):
    fig = Figure(figsize=(5, 4), dpi=80)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    p = fig.gca()
    p.hist(data, bins=int(sqrt(len(data))), rwidth=0.95)
    p.set_xlabel('Wartosc', fontsize=12)
    p.set_ylabel('Liczba wystapien', fontsize=12)
