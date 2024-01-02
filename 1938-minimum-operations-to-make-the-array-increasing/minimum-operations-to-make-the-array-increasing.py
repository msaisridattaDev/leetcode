class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        c=0
        for j in range(1,len(nums)):

            if nums[j]>nums[j-1]:
                pass
            else:
                c+=abs(nums[j]-nums[j-1])+1
                nums[j]=nums[j]+abs(nums[j]-nums[j-1])+1

        return c

            