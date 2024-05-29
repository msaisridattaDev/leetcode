class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        t=[]
        p1=0
        n=0
        for i in nums:
            p=bisect_left(t,i)

            t.insert(p,i)

            if len(t)>=2 and (p==0 or p==len(t)-1):
                
                while t[-1]-t[0]>limit:
                    t.remove(nums[p1])
                    p1+=1


           # print(t,p)

            if len(t)>n:
                n=len(t)

        return n