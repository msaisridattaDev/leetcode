import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0




        '''
        d=[sys.maxsize]*len(nums)
        d[0]=nums[0]
        c={}
        c[d[0]]=[0]
        n=sys.maxsize
        for i in range(1,len(nums)):

            d[i]=d[i-1]+nums[i]

            if d[i] in c.keys():
                c[d[i]]+=[i]
            else:
                c[d[i]]=[i]

        
        print(d,c,n)

        k=target
        if k in nums:
            n=nums.index(k)

        for j in range(len(d)-1,-1,-1):

            y=d[j]-k
            if y in c.keys():

               if  j-c[y][-1] < n:


                    n=j-c[y][-1]
                
        if n!=9223372036854775807:
            return n
        return 0 '''
        