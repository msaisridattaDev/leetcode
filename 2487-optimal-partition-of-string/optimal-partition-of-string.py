class Solution:
    def partitionString(self, s: str) -> int:
        
        p=""
        o=[]
        for i in s:
            if i not in p:
                p+=i
            else:
                o+=[p]
                p=""
                p+=i
                
        o+=[p]

        return len(o)