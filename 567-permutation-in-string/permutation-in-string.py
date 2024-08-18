class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        w=len(s1)

        n=len(s2)

        s1_C=Counter(s1)

        for i in range(n-w+1):

            s2_C=Counter(s2[i:i+w])

            if s1_C==s2_C:
                return True

        return False

