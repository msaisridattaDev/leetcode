
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        u=sum(nums)

        if u%2==0:
            target=u//2
        else:
            return False

        n=len(nums)-1

        d={}

        def canPartition2(nums,n,target):

            if target==0:
                return True
            
            if n <0:
                return 0


            if target <0:
                return 0

            if (n-1,target-nums[n-1]) not in d.keys():
                p=canPartition2(nums,n-1,target-nums[n-1])
                d[(n-1,target-nums[n-1])]=p
            else:
                p=d[(n-1,target-nums[n-1])]

            if p:
                return p

            if (n-1,target) not in d.keys():
                q=canPartition2(nums,n-1,target)
                d[(n-1,target)]=q
            else:
                q=d[(n-1,target)]

            if q:
                return q

            

        return canPartition2(nums,n,target)

        