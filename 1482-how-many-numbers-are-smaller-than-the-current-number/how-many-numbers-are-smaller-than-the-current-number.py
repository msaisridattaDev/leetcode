class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        c={}
        for i,v in enumerate(sorted(nums)):

            if v in c.keys():
                pass
            else:
                c[v]=i
        print(c)

        t=[]
        for j in nums:
            t.append(c[j])

        return t


