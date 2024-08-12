class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans=""
        n=len(s)
        dp=[[False]*n for i in range(n)]

        for i in range(n):
            dp[i][i]=True
            ans=s[i]
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):

                if s[i]==s[j]:

                    if j-1==i or dp[i+1][j-1]==True:
                        dp[i][j]=True

                        if len(ans) < len(s[i:j+1]):
                            ans=s[i:j+1]

        return ans