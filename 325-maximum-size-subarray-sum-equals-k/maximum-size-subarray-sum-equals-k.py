import sys
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d=[sys.maxsize]*len(nums)
        d[0]=nums[0]
        c={}
        c[d[0]]=[0]
        n=-sys.maxsize
        for i in range(1,len(nums)):

            d[i]=d[i-1]+nums[i]

            if d[i] in c.keys():
                c[d[i]]+=[i]
            else:
                c[d[i]]=[i]

        
        #print(d,c)

        if k in c.keys():
            n=c[k][-1]+1

        for j in range(len(d)-1,-1,-1):

            y=d[j]-k
            if y in c.keys():

               if  j-c[y][0] > n:


                    n=j-c[y][0]

                    #print("n is",n,j,c[y],y)
                

        if n>0:
            return n
        return 0
        
