class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        w=[]
        q=0
        for i in s:

            if i=="(":
                w.append(i)
            else:
                if len(w)!=0:
                    w.pop()
                else:
                    q+=1

        
        return len(w)+q