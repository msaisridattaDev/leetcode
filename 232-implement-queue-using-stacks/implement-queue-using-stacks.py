import copy

class MyQueue:

    def __init__(self):
        self.l=[]
        self.q=[]
        

    def push(self, x: int) -> None:
        self.l.append(x)


    def pop(self) -> int:


        if len(self.q)!=0:
            p=self.q.pop()
            return p
        else:
            self.q=copy.deepcopy(self.l[::-1])
            self.l=[]
            p=self.q.pop()
            
            return p

    def peek(self) -> int:

        if len(self.q)!=0:
            return self.q[-1]
        else:
            self.q=copy.deepcopy(self.l[::-1])
            self.l=[]
            return self.q[-1]

    def empty(self) -> bool:
        
        
        if len(self.l)==0 and len(self.q)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()