class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for j in range(1,len(nums)):

            nums[j]=nums[j-1]+nums[j]

        print(nums)
    

        if nums[len(nums)-1]-nums[0]==0:
            return 0
        
        for i in range(1,len(nums)):

            if nums[i-1]== nums[len(nums)-1]-nums[i]:

                return i

        return -1





