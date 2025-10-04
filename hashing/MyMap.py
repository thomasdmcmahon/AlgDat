# General Map class, inherited by both separate chaining and linear probing
class MyMap:
    LOAD_FACTOR_THRESHOLD = 0.75

    def __init__(self):
        self.n = 0
        self.N = 1
        self.A = [None] * self.N
    
    def __loadfactor(self):
        return self.n / self.N
    
    def __rehash(self):
        kvs = [(k,v) for k,v in self]
        self.n = 0
        self.N *= 2
        self.A = [None] * self.N
        for k,v in kvs:
            self[k] = k
    
    def ensurecapacity(self):
        if self.__loadfactor() >= self.LOAD_FACTOR_THRESHOLD:
            self.__rehash()
    
    def __repr__(self):
        kv_strs = [f'{k} ↦ {v}' for k,v in self]
        return '{' + ', '.join(kv_strs) + '}'
