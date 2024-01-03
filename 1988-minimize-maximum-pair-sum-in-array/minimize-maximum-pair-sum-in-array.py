class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()

        p1=0
        p2=len(nums)-1
        t=[]
        while(p1<p2):

            t.append(nums[p1]+nums[p2])
            p2-=1
            p1+=1

        return max(t)

        

        
        