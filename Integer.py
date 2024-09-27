import random as rnd
from GenObject import *

class Integer(GenObject):
    def __init__(self, min, max):
        self.min = min
        self.max = max

        self.instance = self.gen()

    def gen(self):
        return rnd.randint(self.min, self.max)

    def __repr__(self):
        return str(self.instance)
    
# a = Integer(3, 4)
# b = Integer(3, 4)
# print (a, b)
# print (a == b)