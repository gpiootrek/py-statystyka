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
        pass

    def stdev(self):
        pass

    def thirdcm(self):
        pass

    def fourthcm(self):
        pass
