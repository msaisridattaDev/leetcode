class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def is_Interleave(
        s1: str, i: int, s2: str, j: int, s3: str, k: int, memo: list
    ) -> bool:
        
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
        
            if i == len(s1):
                return s2[j:] == s3[k:]
            
            
            if j == len(s2):
                return s1[i:] == s3[k:]
            
            
            if memo[i][j] != -1:
                return memo[i][j] == 1
            
            
            ans = False
            if (i < len(s1) and s1[i] == s3[k] and is_Interleave(s1, i + 1, s2, j, s3, k + 1, memo)) or \
            (j < len(s2) and s2[j] == s3[k] and is_Interleave(s1, i, s2, j + 1, s3, k + 1, memo)):
                ans = True
            
            
            memo[i][j] = 1 if ans else 0
            return ans


        
        if len(s1) + len(s2) != len(s3):
            return False
      
        memo = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        return is_Interleave(s1, 0, s2, 0, s3, 0, memo)