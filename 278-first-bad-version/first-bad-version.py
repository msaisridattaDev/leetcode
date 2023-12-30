# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        h=n
        l=1
        ans=0

        if l==h:
            return l
        while(l<=h):
            
            
            m= int((l+h)/2)

            if isBadVersion(m):
                ans=m
                h=m-1
            else:
                l=m+1

        return ans
             




        