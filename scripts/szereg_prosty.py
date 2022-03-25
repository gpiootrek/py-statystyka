import csv

data = []

class SzeregProsty:
    def __init__(self, data):
        self.headers = ["", ""]
        self.data = data

def open_file(path):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            data.append(float(row[0].replace(',', '.')))
    return SzeregProsty(data)
    