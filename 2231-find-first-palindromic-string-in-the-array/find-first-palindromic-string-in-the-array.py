class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for j in words:

            if j==j[::-1]:
                return j

        return ""