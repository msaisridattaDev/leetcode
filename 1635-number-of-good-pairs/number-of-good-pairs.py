class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        c={}
        for i in range(len(nums)):
            if nums[i] in c.keys():
                c[nums[i]]+=[i]
            else:
                c[nums[i]]=[i]
        
        print(c)

        p=0
        for h in c.values():

            if len(h)==2:
                p+=1
            else:
                p+=((len(h)-1)*len(h))/2

        return int(p)

        
