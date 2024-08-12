class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        l=[]

        for t in num:
            while l and k>0 and l[-1]>t:
                l.pop()
                k-=1
            l.append(t)

       # print(l,k)
        n=len(l)
        if k>0:
            l=l[0:n-k]
            s="".join(l)

        s="".join(l).lstrip('0')
        
        if s:
            return s
        return "0"

