class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1


        while(l<=h):

            m= int((l+h)/2)

            #print(l,m,h)
            if (0<=m-1 and m+1<=len(nums)-1) and nums[m-1]<nums[m]>nums[m+1]:
                return m
            elif m+1<=len(nums)-1 and nums[m+1]>nums[m]:
                l=m+1
            elif 0<=m-1 and nums[m-1]>nums[m]:
                h=m-1
            else:
                break
            
        return m