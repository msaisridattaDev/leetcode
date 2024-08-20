class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        d=[None]*len(nums)
        d[0]=nums[0]

        c=0
        t={}
        if d[0]==k:
            c+=1
        t[d[0]]=[0]

    
        for i in range(1,len(nums)):

            



            d[i]=d[i-1]+nums[i]

            if d[i]==k:
                c+=1
            if d[i]-k in t.keys():
                c+=len(t[d[i]-k])

            if d[i] not in t.keys():
                t[d[i]]=[i]
            else:
                t[d[i]]+=[i]
            
            

        
        #print(t,d)



  
 

        return c

        
            







            