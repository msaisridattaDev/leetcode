class MRUQueue:

    def __init__(self, n: int):
       self.d=list(range(1,n+1))


    def fetch(self, k: int) -> int:
       
        v=self.d.pop(k-1)
        self.d.append(v)
        return v
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)