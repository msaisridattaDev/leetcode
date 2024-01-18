class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        t=[nums[0]]
        a=[]
        p=1

        while(p<=len(nums)-1):
            #print(min(t),nums[p],t)
            if nums[p]-t[0]<=k:
                t.append(nums[p])
                #print(t)
            else:
                a+=[t]
                t=[nums[p]]
            

            p+=1
        a.append(t)

        #print(a)

        return len(a)

