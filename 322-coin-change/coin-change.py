class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d={}

    
        def count(coins, n, sum,dist):

            # If sum is 0 then there is 1
            # solution (do not include any coin)
            
            #print(n,sum)
            if (sum == 0):
                return 0

            # If sum is less than 0 then no
            # solution exists
            if (sum < 0):
                return -1

            # If there are no coins and sum
            # is greater than 0, then no
            # solution exist
            if (n <= 0):
                
                return -1

            if (n-1,sum) not in d.keys():
                p=count(coins, n - 1, sum,dist)
                
                d[(n-1,sum)]=p
            else:
                p=d[(n-1,sum)]


            if (n, sum-coins[n-1]) not in d.keys():
                
                q=count(coins, n, sum-coins[n-1],dist+1)
            
                d[(n, sum-coins[n-1])]=q
            else:
                q=d[(n, sum-coins[n-1])]

            
            if p==None or q==None:
                
                if p:
                    return p
                if q:
                    return q

            if q<0 and p>=0:
                return p
            elif p<0 and q>=0:
                return q+1
            elif p>=0 and q>=0:


                if p<q+1:
                    return p
                return q+1
            elif p <0 and q <0:
                return -1
        
        return count(coins,len(coins),amount,0)