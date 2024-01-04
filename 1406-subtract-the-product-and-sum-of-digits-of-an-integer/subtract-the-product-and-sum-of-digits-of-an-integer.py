class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        p=10**int(len(str(n))-1)
        a=1
        a2=0
        while(n>=0 and p>0):
            q=int(n/p)
            a=a*q
            a2+=q
            n-=q*p
            p=int(p/10)

        return a-a2

