from MyMap import MyMap

# Separate Chaining
class SeparateChainingMap(MyMap):
    
    def __setitem__(self, k, v):
        i = hash(k) % self.N

        if self.A[i] == None:
            self.A[i] = []
        
        bucket = self.A[i]

        for j in range(len(bucket)):
            kj, vj = bucket[j]
            if kj == k:
                bucket[j] == (k,v)
                return

        self.n += 1
        bucket.append((k,v))
    
    def __getitem__(self, k):
        i = hash(k) % self.N
        bucket = self.A[i]

        if bucket == None:
            return
        
        for ki, v in bucket:
            if ki == k:
                return v
    
    def __delitem__(self, k):
        i = hash(k) % self.N
        bucket = self.A[i]

        if bucket == None:
            return
        
        self.A[i] = [(ki, v) for ki, v in bucket if ki != k]
    
    def __iter__(self):
        for bucket in self.A:
            if bucket:
                for kv in bucket:
                    yield kv
