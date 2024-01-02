import sys
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        n=-sys.maxsize
        p=-sys.maxsize
        d=0
        p=0
        for i,v in enumerate(nums):
            
            
            if v>0:
                if p<=0:
                    p=len(nums[i:])
            elif v<0:
                n=i
        if n>=0:
            d=len(nums[0:n])+1
        #print(d,p)
        
        return max(d,p)
