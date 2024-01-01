class MovingAverage:

    def __init__(self, size: int):
        self.l=[]
        self.size=size

    def next(self, val: int) -> float:
        self.l.append(val)
        
        return sum(self.l[-1:-(self.size+1):-1])/len(self.l[-1:-(self.size+1):-1])
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)