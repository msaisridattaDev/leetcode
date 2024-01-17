class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        

        c={}
        nums.sort()
        for j in nums:

            if j in c.keys():
                c[j]+=1
            else:
                c[j]=1

        if len(nums)>nums[-1]:
            b=len(nums)
        else:
            b=nums[-1]

        q=len(nums)-len(set(nums))
        
        d=set(range(1,b+q))-set(nums)

        f=list(d)
        f.sort()



        p=0
        w=0

        while(p<=len(nums)-1):

            v=nums[p]
            h=nums[p]

            while(c[h]>1):

                
                y=f.pop(0)

                if  y>v:
                    w+=abs(v-y)

                    c[h]-=1
                    c[y]=1
 

            p+=1

        return w
        
        return 1








        return 6