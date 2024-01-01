class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p1=0
        p2=len(nums)-1

        while(p1!=p2 and p1<p2):


            if nums[p1]%2!=0 and nums[p2]%2==0:
                temp=nums[p2]
                nums[p2]=nums[p1]
                nums[p1]=temp

            elif nums[p1]%2==0 and nums[p2]%2!=0:
                p1+=1
                p2-=1

            elif nums[p1]%2!=0 and nums[p2]%2!=0:
                p2-=1

            elif nums[p1]%2==0 and nums[p2]%2==0:
                p1+=1

        return nums

                
        