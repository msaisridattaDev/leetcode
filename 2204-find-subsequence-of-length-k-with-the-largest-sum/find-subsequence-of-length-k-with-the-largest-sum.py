
import copy
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        l=[]
        z=copy.deepcopy(nums)
        q=[]
        
        while(k>0):
            p=max(nums)
            g=nums.index(p)
            l.append(p)
            
            nums.pop(g)
            k-=1

        
        for i in z:
            
            if i in l:
                q.append(i)
                l.remove(i)
            

        
        return q