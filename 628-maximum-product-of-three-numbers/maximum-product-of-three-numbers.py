class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
       
        nums.sort()
        p=nums[0]*nums[1]*nums[-1]
        q=nums[-1]*nums[-2]*nums[-3]

        if  p > q:
           return p
        return q