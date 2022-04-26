import math


class Statistics:
    def __init__(self, data):
        self.data = data
        self.mean = self.mean()
        self.stdev = self.stdev()
        self.wspzm = round((self.stdev / self.mean) * 100, 2)
        self.wspasm = round(self.thirdcm() / self.stdev**3, 2)
        self.kurtoza = round(self.fourthcm() / self.stdev**4, 2)

    def count(self):
        counter = 0
        for key in self.data:
            counter += self.data[key]
        return counter

    def mean(self):
        sum = 0
        for key in self.data:
            sum += key*self.data[key]
        return sum / self.count()

    def stdev(self):
        sum = 0
        for key in self.data:
            sum += (key-self.mean)**2
        return math.sqrt(sum/self.count())

    def thirdcm(self):
        sum = 0
        for key in self.data:
            sum += (key - self.mean)**3
        return sum / self.count()

    def fourthcm(self):
        sum = 0
        for key in self.data:
            sum += (key - self.mean)**4
        return sum / self.count()