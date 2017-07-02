from random import gauss

class Implementation:

    def __init__(self, esperance, variance):
        self.esperance = esperance
        self.variance = variance

    def __str__(self):
        s = "Esperance : " + str(self.esperance) + "\n"
        s += "Variance : " +str(self.variance) + "\n"
        return (s)

    def tirerBras(self):
        return self.variance * gauss(0, 1) + self.esperance




