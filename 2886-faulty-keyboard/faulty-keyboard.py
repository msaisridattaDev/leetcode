class Solution:
    def finalString(self, s: str) -> str:

        p=""
        for i in s:
            if i=="i":
                p=p[::-1]
            else:
                p+=i

        return p

        