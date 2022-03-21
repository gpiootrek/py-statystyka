import csv

headers = []
data = {}

def open_file(path):
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
    print(headers)
    print(data)
    