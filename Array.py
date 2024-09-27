from Integer import *
from GenObject import *

class Array(GenObject):
    def __init__(self, length, elem_gen, endl=False):
        self.length = length
        self.elem_gen = elem_gen
        self.endl = endl

        self.instance = self.gen()

    def gen(self):
        return [self.elem_gen() for i in range(self.length)]

    def __repr__(self):
        if self.endl:
            return '\n'.join(map(str, self.instance))
        else:
            return ' '.join(map(str, self.instance))
        
    def __getitem__(self, key):
        return self.instance[key]
        
# a = Array(length = 10, elem_gen = Integer(3, 7).gen, endl=False)
# print(a)
# print(a[3])
