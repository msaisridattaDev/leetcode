class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i,v in enumerate(nums):
            nums[i]=[nums[i],i]
        
        nums.sort()

        p1=0
        p2=1
        while(p2<=len(nums)-1):

            print(p1,p2)
            if nums[p1][0]==nums[p2][0]:

                if nums[p2][1]-nums[p1][1] <=k:
                    return True
                else:
                    p2+=1
                    p1+=1
            else:
                p1+=1
                p2+=1

        return False

        