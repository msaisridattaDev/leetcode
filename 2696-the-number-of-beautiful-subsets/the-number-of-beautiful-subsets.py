class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # Sort the array to simplify logic for subsets and differences
        nums.sort()
        
        # Memoization to avoid recalculating the same subset
        memo = {}
        
        def dfs(index, subset):
            if index == len(nums):
                return 1  # Base case: a valid subset
            
            # Create a state based on current index and subset
            state = (index, tuple(subset))
            if state in memo:
                return memo[state]
            
            # Count subsets that exclude the current element
            count = dfs(index + 1, subset)
            
            # Check if we can include the current element
            if all(abs(num - nums[index]) != k for num in subset):
                count += dfs(index + 1, subset + [nums[index]])
            
            memo[state] = count
            return count
        
        # Subtract 1 to exclude the empty subset
        return dfs(0, []) - 1