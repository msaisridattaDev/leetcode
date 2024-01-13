class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c={}
        w=0

        for i in s:
            if i in c.keys():
                c[i]+=1
            else:
                c[i]=1

        for  j in t:

            if j in c.keys() and c[j]>0:

                c[j]-=1
            else:
                w+=1
        
        

        return w
        


                


        
