class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        o=original
        def findFinalValue(nums,o) -> int:

            if o in nums:
                o=o*2
            else:
                return o
            return findFinalValue(nums,o)

        return findFinalValue(nums,o)