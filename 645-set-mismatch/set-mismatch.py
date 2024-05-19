class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c={}
       
        for i in nums:

            if i in c.keys():
                c[i]+=1
            else:
                c[i]=1

        for j in range(1,len(nums)+1):


            if j not in c.keys():
                q=j
            elif c[j]==2:
                p=j

        return [p,q]

