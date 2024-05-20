class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]

        for i,v in enumerate(nums):

            p=abs(v)-1
            
            if nums[p] <0 and p <= len(nums)-1:
                l.append(abs(v))
            else:
                nums[p]=-nums[p]


        return l