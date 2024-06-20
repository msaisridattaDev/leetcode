class Solution:
    def rob(self, nums: List[int]) -> int:
        d=[0]*len(nums)

        d[0]=nums[0]

        
        
        if len(nums)>1:
            d[1]=max(nums[0],nums[1])

        for i in range(2,len(nums)):

            d[i]=max(d[i-1],d[i-2]+nums[i])

        return d[-1]
        