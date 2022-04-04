import math


class Statistics:
    def __init__(self, data, count):
        self.data = data
        self.mean = self.mean()
        self.count = 0
        for key in self.data:
            self.count += self.data[key]
        self.stdev = self.stdev()
        self.wspzm = round((self.stdev / self.mean) * 100, 2)
        self.wspasm = round(self.thirdcm() / self.stdev**3, 2)
        # self.median()

    def median(self):
        pass

    def mean(self):
        sum = 0
        for key in self.data:
            sum += key*self.data[key]
        return sum / self.count

    def stdev(self):
        sum = 0
        for key in self.data:
            sum += (key-self.mean)**2
        return math.sqrt(sum/self.count)

    def thirdcm(self):
        sum = 0
        for key in self.data:
            sum += (key - self.mean)**3
        return sum / self.count
