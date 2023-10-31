class Solution:
    def canJump(self, nums: List[int]) -> bool:
        global v
        v=[False]*len(nums)
        global d

        d=[None]*len(nums)
        def jumpGame(nums,i,d,v):


            if v[i]==False:
                v[i]=True
            
            if i==len(nums)-1:
                if d[i]==None:
                    d[i]=True
                    return True

            for j in range(nums[i],0,-1):

                if i+j<= len(nums)-1:
                    #print(i+j)
                    if v[i+j]==False:
                        if d[i+j]==None:
                            if jumpGame(nums,i+j,d,v):
                                d[i]=True
                                #print(d)
                                return True       
                

        jumpGame(nums,0,d,v)
        return d[0]
        