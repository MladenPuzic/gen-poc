from Array import *
from random import *

class DistinctArray(Array):
    def __init__(self, length, elem_gen, endl=False):
        super().__init__(length, elem_gen, endl)

        self.instance = self.gen()

    def gen(self):
        inserted = set()
        for i in range(self.length):
            elem = self.elem_gen()
            while elem in inserted:
                elem = self.elem_gen()
            inserted.add(elem)
        ans = list(inserted)
        shuffle(ans)
        return ans

# print(DistinctArray(length = 10, elem_gen = Integer(1, 10).gen))