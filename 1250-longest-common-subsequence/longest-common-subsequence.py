class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        

        s=text1
        r=text2

        m=len(s)
        n=len(r)
        
        dp=[]
        for i in range(len(s)):
            temp=[]
            for j in range(len(r)):

                temp.append(0)

            dp.append(temp)

        for i in range(len(s)):
        
            for j in range(len(r)):
                if s[i]==r[j]:

                    if 0<=i-1<=m-1 and 0<=j-1<=n-1:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=1

                    
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        return dp[m-1][n-1]

        
        
            