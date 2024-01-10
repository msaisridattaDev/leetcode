class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        p1=int(event1[0].lstrip("0").replace(":",""))
        p2=int(event1[1].lstrip("0").replace(":",""))
        
        w1=int(event2[0].lstrip("0").replace(":",""))
        w2=int(event2[1].lstrip("0").replace(":",""))
        
       # print(p1,p2,w1,w2)
        
        
        if w1<=p1<=w2:
            return True
        elif w1<=p2<=w2:
            return True
        if p1<=w1<=p2:
            return True
        elif p1<=w2<=p2:
            return True
        
        
        #print(p1,p2,w1,w2)
        
        return False
        
    
            
            

        