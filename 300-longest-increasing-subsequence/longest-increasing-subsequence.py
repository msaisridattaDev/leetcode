class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        v=[False]*len(nums)

        d=[0]*len(nums)

        print(v,d)

        def lengthOfLIS(nums,d,v,i):

            if v[i]:
                return d[i]
            else:
                v[i]=True

            if i==len(nums)-1:
                d[i]=1
                return 1

            for j in range(i+1,len(nums)):
                if nums[j]> nums[i]:
                    p=lengthOfLIS(nums,d,v,j) 
                    if p+1> d[i]:
                        d[i]=1+p
                
            if  d[i]==0:
                d[i]=1
  
            return d[i]

        for i in range(len(nums)):
            lengthOfLIS(nums,d,v,i)

        return max(d)