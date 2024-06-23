class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                if tuple(nums[:]) not in t.keys():
                    t[tuple(nums[:])]=1
                return
            
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1, end)  # Recurse
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo swap)

        t = {}
        backtrack(0, len(nums))
        return t