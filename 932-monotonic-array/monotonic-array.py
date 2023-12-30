class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if nums[-1]>=nums[0]:
            pass
        else:
            nums.reverse()

    
        for j in range(1,len(nums)):
            if nums[j]>=nums[j-1]:
                pass
            else:
                return False

        return True


        
        
        





        