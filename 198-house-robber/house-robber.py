class Solution:
    def rob(self, nums: List[int]) -> int:
        d=[0]*len(nums)

        d[0]=nums[0]

        if len(nums)>1:
            d[1]=nums[1]
        
        if len(nums)==2:
            d[1]=max(d[0],d[1])

        for i in range(2,len(nums)):

            d[i]=max(d[i-1]-nums[i-1]+nums[i],d[i-2]+nums[i])

        print(d)

        return max(d)
        