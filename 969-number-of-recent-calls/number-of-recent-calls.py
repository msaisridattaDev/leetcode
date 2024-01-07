class RecentCounter:

    def __init__(self):
        self.l=[]
        self.p1=0
    def ping(self, t: int) -> int:
        
        self.l.append(t)
        
        while(self.p1<=len(self.l)-1 and self.l[-1]-self.l[self.p1]>3000 ):
            #print(self.p1)
            self.p1+=1
       # print(self.p1,len(self.l[self.p1::]),self.l)
        return len(self.l[self.p1::])


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)