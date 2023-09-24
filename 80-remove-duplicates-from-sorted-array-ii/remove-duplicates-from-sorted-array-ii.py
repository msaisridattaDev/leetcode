class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        p1=0
        p2=1
        c=0
        while(len(nums)-1 >=p2):
            if nums[p1]==nums[p2]:
                c+=2
                if c> 2:
                    nums.pop(p2)
                    c-=1
                    print(nums,p1,p2)

                else:
                    prev=nums[p1]
                    p1+=1
                    p2+=1

            else:
                c=0
                p1+=1
                p2+=1

                    
                
        return len(nums)


            
        