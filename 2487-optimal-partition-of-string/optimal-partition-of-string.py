class Solution:
    def partitionString(self, s: str) -> int:
        
        p=""
        c=0
        for i in s:
            if i not in p:
                p+=i
            else:
                c+=1
                p=""
                p+=i
                
        c+=1

        return c