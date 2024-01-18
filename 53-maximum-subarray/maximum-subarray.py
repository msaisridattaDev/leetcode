
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        r=0
        m=-sys.maxsize

        for i in nums:

            if r+i >= i:
                r+=i
            else:
                r=i

            if m < r:
                m=r

        return m

        


