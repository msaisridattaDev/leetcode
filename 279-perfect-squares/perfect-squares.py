class Solution:
    def numSquares(self, n: int) -> int:

        l=[]
        def getPerfectSquaresList(n,l):
            p=1
            i=1

            while(p<=n):
                p=p*p
                if p<=n:
                    l.append(p)
                i+=1
                p=i
            return l
        coins=getPerfectSquaresList(n,l)


        amount=n
        d={}

    
        def coinChange(coins: List[int], amount: int) -> int:
            # classical 1d DP problem
            # 1. define the DP array 
            # D[i] contains the fewest number of coins that needed to make up amount i where 0 <= i < amount, len(D) = n+1
            length = amount + 1
            large = 100000000
            
            # 2. define recurrence and boundary condition
            # D[i] = min(D[j] + 1, D[i]) for j in range(i) and j+ x = i, where x in coins
            D = length * [large]
            D[0] = 0

            for i in range(0, length):
                for x in coins:
                    if i >= x:
                        j = i - x
                        D[i] = min(D[j] + 1, D[i])

            if D[-1] == large:
                return -1
                
            return D[-1]

        return coinChange(coins, amount)

    

        

        


        