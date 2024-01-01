class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        nums.append(987654321)
        p1=0
        p2=1
        t=[]
        c=1
        h=0
        b=[]  
        while(p2<=len(nums)-1):
                    
            if  nums[p2]-nums[p1]==1:
                c+=1
                p1+=1
                p2+=1
            else:
                t.append(c)       
                c=1
                p1+=1
                p2+=1

        #print(t,nums)

        h=0

        for j in t:

            if j==1:
                b.append(str(nums[h]))
                h+=1
            else:
                b.append(str(nums[h])+"->"+str(nums[h+j-1]))
                h+=j

        return b


            





