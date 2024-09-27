class GenObject():
    def __eq__(self, other):
        return self.instance == other.instance
    
    def __hash__(self):
        return hash(self.__repr__())