from Integer import *
from DistinctArray import *

class Permutation(DistinctArray):
    def __init__(self, length, start = 1, endl = False):
        super().__init__(length, Integer(start, start+length-1).gen, endl)

print(Permutation(length = 10))
#print(Permutation(length = 15).gen())