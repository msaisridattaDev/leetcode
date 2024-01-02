import sys
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        s=nums[0]
        m=-sys.maxsize

        for i in range(len(nums)):
            
            if nums[i] <s:
                s=nums[i]

            if nums[i]-s >=m:
                m=nums[i]-s

        if m <=-1 or m==0:
            return -1
        return m