class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        l=list(range(1,n+1,1))
        
        def findTheWinner2(l, k: int):

            if len(l)==1:
                return l

            if len(l) >k:
                p=k-1
            else:
                p= k%len(l) -1
            
            if p <0:
                p=len(l)+p

            l=l[p+1::]+l[0:p]
            #print(l)

            if len(l)!=1:
                return findTheWinner2(l,k)
            else:
                return l


            return l

        ans=findTheWinner2(l, k)

        return ans[0]

