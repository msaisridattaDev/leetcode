class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        s=0
        def numberOfMatches(n,s):

            if n==1:
                return s

            if n%2==0:
                p=int(n/2)
                s+=p
            else:
                p= int((n-1)/2)
                s+=p

            return numberOfMatches(n-p,s)

        return numberOfMatches(n,s)
            

