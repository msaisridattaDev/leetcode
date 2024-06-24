class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d=[0]*len(nums)
        t={}
        ans=0
        if nums[0]==0:
            d[0]=-1
            t[-1]=0
        else:
            d[0]=1
            t[1]=0

        
        for i in range(1,len(nums)):

            if nums[i]==0:
                d[i]=d[i-1]+-1
                if d[i] in t.keys():
                    if i-t[d[i]]>ans:
                        ans=i-t[d[i]]
                elif d[i]==0 and 0 not in t.keys():
                    if i+1>ans:
                        ans=i+1
                else:
                    t[d[i]]=i

            else:
                d[i]=d[i-1]+1

                if d[i] in t.keys():
                    if i-t[d[i]]>ans:
                        ans=i-t[d[i]]
                elif d[i]==0 and 0 not in t.keys():
                    if i+1>ans:
                        ans=i+1
                else:
                    t[d[i]]=i


        
        return ans

