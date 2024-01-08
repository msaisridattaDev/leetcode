class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        c={}
    
        for j in text:

            if j in c.keys():
                c[j]+=1
            else:
                c[j]=1

        n=["b","a","l","l","o","o","n"]

        w=0
        while(1):

            p=n.pop(0)
            
            if p in c.keys() and c[p]>0:
                c[p]-=1

            else:
                break

            if len(n)==0:
                n=["b","a","l","l","o","o","n"]
                w+=1

                
        return w