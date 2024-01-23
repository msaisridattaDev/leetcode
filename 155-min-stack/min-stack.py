class MinStack:

    def __init__(self):  
        self.l=[]
    def push(self, val: int) -> None:
        
        if len(self.l)>0:
            r=self.l.pop()
            self.l.append(r)

            if r[1]< val:
                self.l.append([val,r[1]])
            else:
                self.l.append([val,val])
        
        else:
            self.l.append([val,val])

    def pop(self) -> None:

        
        if len(self.l)>0:
            self.l.pop()
        

        

    def top(self) -> int:
        
        
        if len(self.l)>0:
            w=self.l.pop()
            self.l.append(w)
            return w[0]

    def getMin(self) -> int:

        if len(self.l)>0:
            return self.l[-1][1]




        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()