class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        t=[]
        p=0
        while(1):
            



            if p<=len(nums)-1:


                
                if p+2<=len(nums)-1 and nums[p+2]-nums[p]<=k:
                    
                    pass
                elif p+2<=len(nums)-1 and nums[p+2]-nums[p]>k: 
                    #print(nums[p+2],nums[p],p+2,p)
                    return []
                t+=[nums[p:p+3]]
                p=p+3
            

            else:
                break

        #print(t)
        return t
