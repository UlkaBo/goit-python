import pickle
from collections import UserDict
class Di(UserDict):
    def add_rec(self, r):
        self[r.name] = r
        

    def __getstate__(self):
        atr = self.__dict__
        
        
        return atr

    def __setstate__(self, atr):
        self.__dict__ = atr

    
class R():
    def __init__(self, n):
        self.value = [1,4,5,6,'dt', n]
        self.c = 2
        self.r = 4
        self.name = 'qwe'
    
class N():
    def __init__(self):
        self.value = '345345'
