import math


class Statistics:
    def __init__(self, data, stdev, mean):
        self.data = data
        self.stdev = stdev
        self.mean = mean
        self.wspzm = round((self.stdev / self.mean) * 100,2)
        self.wspasm = round(self.thirdcm() / stdev**3,2)
    
    def thirdcm(self):
        sum = 0
        for el in self.data:
            sum += (el - self.mean)**3
        return sum/len(self.data)