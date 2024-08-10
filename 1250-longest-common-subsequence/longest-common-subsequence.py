class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        s=text1
        r=text2

        m=len(s)
        n=len(r)
        
        dp=[[0]*(n+1) for h in range(m+1)]
        

        for i in range(1,m+1):
        
            for j in range(1,n+1):
                if s[i-1]==r[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        return dp[m][n]

        
        
            