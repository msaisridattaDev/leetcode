class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        c=nums[0]
        for i in range(1,len(nums)):

            c+=nums[i]
            nums[i]=c

        return nums