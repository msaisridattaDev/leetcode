class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[None]*(n+1)

        dp[0]=1
        dp[1]=1
        
        if n>=2:   
            dp[2]=2
            for i in range(3,n+1):
                dp[i]=dp[i-1]+dp[i-2]

        print(dp,len(dp))

        return dp[n]
    
        

        



        