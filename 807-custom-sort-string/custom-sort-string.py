class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        c={}
        a={}
        t=[]
        for i,v in enumerate(order):

            c[v]=i
            a[i]=v

        p=""
        ans=""
        for j in s:
            if j in c.keys():
                t.append(c[j])
            else:
                p+=j
        t.sort()
        #print(t,a)
        for h in t:
            ans+=a[h]

            

        return ans+p

        #return "cbad"

            
        