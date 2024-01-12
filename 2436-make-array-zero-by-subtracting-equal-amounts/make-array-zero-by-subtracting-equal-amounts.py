class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
                
        v=[0]*len(nums)
        c=0

        u=0   
        while(u<=len(nums)-1):
            if nums[u]==0:
                nums.pop(u)
                u-=1
            u+=1

        print(nums)
        if nums==None:
            return 0

        while(nums!=v and nums!=[]):
            p=[]
            q=min(nums)
            print(q)
            for x in nums:
                if x!=0:
                    if x-q<=0:
                        pass
                    else:
                        p.append(x-q)
            print(p)
            nums=p
            c+=1

        return c
