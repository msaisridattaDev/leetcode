import sys

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        p1=0
        p2=len(nums)-1
        ans=-sys.maxsize
        
        print(nums)
        while(p2>p1):

            #print(nums[p1],nums[p2])
            if nums[p1]<0:


                if nums[p1]<0 and nums[p2]<0:
                    break 

                if -(nums[p1])> nums[p2]:
                    p1+=1

                elif -(nums[p1]) < nums[p2]:
                    p2-=1

                elif -(nums[p1]) == nums[p2]:

                    if nums[p2] > ans:
                        ans=nums[p2]
                        return ans

            elif nums[p1]>0 and nums[p2]>0:
                    break

                
        

            #print(p1,p2)
            

        return -1

                