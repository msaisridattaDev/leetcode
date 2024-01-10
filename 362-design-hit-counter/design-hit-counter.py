class HitCounter:

    def __init__(self):
        self.l=[]

    def hit(self, timestamp: int) -> None:
        self.l.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:

        if len(self.l)>0:
            p=self.l.pop(0)
        else:
            return 0
        flag=False
        #print(self.l,timestamp)
        if timestamp-p>=300:
            
            while(timestamp-p>=300):
                if len(self.l)>0:
                    p=self.l.pop(0)
                    #print(p)
                else:
                    flag=True
                    break
            
            if not flag:
                self.l=[p]+self.l
        else:
            self.l=[p]+self.l
        return len(self.l)



        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)