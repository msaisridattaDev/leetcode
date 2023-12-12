class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        y=needle[0]
        p=len(needle)

        t={y:[]}

        for j in range(len(haystack)):

            if haystack[j]==y:
                t[haystack[j]]+=[j]

        for i in t[y]:

            if haystack[i:i+p]==needle:
                return i


        return -1

        