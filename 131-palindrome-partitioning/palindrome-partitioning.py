class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        
        # Step 1: Create a DP table to store whether s[i:j] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        # Single letters are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for two-character palindromes
        for i in range(n - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])

        # Check palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        # Step 2: Backtracking to find all palindromic partitions
        def backtrack(start: int, path: list, result: list):
            if start == n:
                result.append(path[:])  # Append a copy of the current path
                return
            
            for end in range(start, n):
                if dp[start][end]:  # If s[start:end+1] is a palindrome
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path, result)
                    path.pop()  # Backtrack
        
        result = []
        backtrack(0, [], result)
        return result
        