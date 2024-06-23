
import sys
class Solution:
    def jump(self, nums: List[int]) -> bool:
   
        v=[False]*len(nums)
        d=[sys.maxsize]*len(nums)
        def jumpGame(nums,i,d,v):


            #print(i)
            if v[i]==False:
                v[i]=True
            
            if i==len(nums)-1:
                if d[i]==sys.maxsize:
                    d[i]=0
                    return d[i]

            for j in range(nums[i],0,-1):

                if i+j<= len(nums)-1:
                    if v[i+j]==False:
                        if d[i+j]==sys.maxsize:
                            p=jumpGame(nums,i+j,d,v)

                            if d[i] > p+1:
                                d[i]=p+1 
                            #print(nums[i],nums[i+j],d[i],p)
                    else:
                        p=d[i+j]
                        if d[i] > p+1:
                            d[i]=p+1 

                        
            return d[i]       
                

        jumpGame(nums,0,d,v)
        return d[0]


        
        