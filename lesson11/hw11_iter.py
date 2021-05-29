from collections import UserDict

class C(UserDict):
    def __next__(self):

        if self.i >= len(self):
            raise StopIteration
        
        l = list(self.items())
        a = dict(l[self.i : self.i + self.N])
        self.i += self.N
        
        return a
    
    def __iter__(self, N=2):
        self.i = 0
        self.N = N
        return self

c = C()
c.data = {4:5, 6:7, 8:9, 0:1, 2:3}
for e in c: print(e, 'end')
