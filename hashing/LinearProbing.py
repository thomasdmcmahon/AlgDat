from MyMap import MyMap

class LinearProbingMap(MyMap):

    def __setitem__(self, k, v):
        self.ensurecapacity()

        i = hash(k) % self.N

        while self.A[i] != None:
            ki, _ = self.A[i]
            if k == ki:
                self.A[i] = (k,v)
                return
            i = (i + 1) % self.N

        self.n += 1
        self.A[i] = (k, v)
    
    def __getitem__(self, k):
        i = hash(k) % self.N

        while self.A[i] != None:
            ki, vi = self.A[i]
            if k == ki:
                return vi
            i = (i + 1) % self.N
    
    def __delitem__(self, k):
        i = hash(k) % self.N

        while self.A[i] != None:
            ki, _ = self.A[i]
            if k == ki:
                self.n -= 1
                self.A[i] = None
                self.__fill_hole(i)
                return
            i = (i + 1) % self.N
    
    def __fill_hole(self, i):
        s = 1
        while self.A[(i + s) % self.N] != None:
            k, v = self.A[(i + s) % self.N]
            j = hash(k) % self.N
            if not(0 < (j-i) % self.N <= s):
                self.A[i] = (k, v)
                self.A[(i + s) % self.N] = None
                self.__fill_hole((i + s) % self.N)
                return
            s += 1
    
    def __iter__(self):
        for kv in self.A:
            if kv != None:
                yield kv  
