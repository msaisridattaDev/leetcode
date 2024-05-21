import sys
class Solution:
    def tribonacci(self, n: int) -> int:
        
        d=[-sys.maxsize]*(n+3)

        d[0]=0
        d[1]=1
        d[2]=1
        def tribonacci(n,i,d):

            if i>=n+1:
                return d[n]


            if d[i]==-sys.maxsize:
                d[i]=d[i-1]+d[i-2]+d[i-3]
            

            return tribonacci(n,i+1,d)

        return tribonacci(n,0,d) 


