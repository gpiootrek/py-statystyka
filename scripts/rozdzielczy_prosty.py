import csv

headers = []
data = {}

class SzeregProsty:
    pass

def open_file(path):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        row_index = 1
        for row in csv_reader:
            if row_index == 1:
                headers = row
            else:
                if("," in row[0] or "," in row[1]):
                    data[float(row[0].replace(',', '.'))] = float(row[1].replace(',', '.'))                    
                else:
                    data[float(row[0])] = float(row[1])
            row_index+=1
    print(headers)
    print(data)