#######3#####

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
       
        stack = []
        total_sum = 0
     
        for i in range(n):
       
            while stack and stack[-1][0] > arr[i]:
                value, index = stack.pop()
   
                prev_index = stack[-1][1] if stack else -1
                count = (index - prev_index) * (i - index)
                total_sum += value * count
                total_sum %= MOD
            
      
            stack.append((arr[i], i))

        
        while stack:
            value, index = stack.pop()
            prev_index = stack[-1][1] if stack else -1
            count = (index - prev_index) * (n - index)  # Remaining elements to the right
            total_sum += value * count
            total_sum %= MOD

        return total_sum