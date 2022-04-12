import math


# TODO wzory na szereg rozdzielczy przedzialowy
class Statistics:
    def __init__(self, data):
        self.data = data
        self.mean = self.mean()
        self.stdev = self.stdev()
        self.wspzm = round((self.stdev / self.mean) * 100, 2)
        self.wspasm = round(self.thirdcm() / self.stdev**3, 2)

    def count(self):
        counter = 0
        for key in self.data:
            counter += self.data[key]
        return counter

    def median(self):
        pass

    def mean(self):
        counter = 0
        sum = 0
        for key in self.data:
            counter += self.data[key]
            sum += ((key[0] + key[1]) / 2) * self.data[key]
        return sum / counter

    def stdev(self):
        counter = 0
        sum = 0
        for key in self.data:
            counter += self.data[key]
            sum += (((key[0] + key[1]) / 2) - self.mean)**2 * self.data[key]
        return math.sqrt(sum / counter)

    def thirdcm(self):
        counter = 0
        sum = 0
        for key in self.data:
            counter += self.data[key]
            sum += (((key[0] + key[1]) / 2) - self.mean)**3 * self.data[key]
        return sum / counter

    def fourthcm(self):
        counter = 0
        sum = 0
        for key in self.data:
            counter += self.data[key]
            sum += (((key[0] + key[1]) / 2) - self.mean)**4 * self.data[key]
        return sum / counter
