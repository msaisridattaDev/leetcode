class Solution:
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        memo = [[-1] * (2 * total + 1) for _ in range(len(nums))]
        
        return self.calculate(nums, 0, 0, S, total, memo)

    def calculate(self, nums, i, sum, S, total, memo):
        if i == len(nums):
            return 1 if sum == S else 0
        
        # Check the memoization table
        if memo[i][sum + total] != -1:
            return memo[i][sum + total]
        
        # Calculate ways by adding and subtracting the current number
        add = self.calculate(nums, i + 1, sum + nums[i], S, total, memo)
        subtract = self.calculate(nums, i + 1, sum - nums[i], S, total, memo)
        
        # Store the result in the memoization table
        memo[i][sum + total] = add + subtract
        return memo[i][sum + total]

        