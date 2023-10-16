class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h=len(nums)-1
        l=0
        p=len(nums)-1
        b=False
        while(l<=h and b!=True):
            m=int((l+h)/2)
            
            if  target==nums[m]: 
                b=True
                return m
            print(l,h,m)
            if nums[m]< target and target > nums[-1]:
                if nums[m]> nums[-1]: 
                    l=m+1
                else:
                    h=m-1
            
            elif nums[m]>= target and target > nums[-1]: 
                    h=m-1
            
            elif nums[m]< target and target <= nums[-1]:
                    l=m+1
            
            elif nums[m]> target and target <= nums[-1]:
                if nums[m]<nums[-1]: 
                    h=m-1
                else:
                    l=m+1

               
        if b:
            return m
        return -1
                
        
               
       
            
