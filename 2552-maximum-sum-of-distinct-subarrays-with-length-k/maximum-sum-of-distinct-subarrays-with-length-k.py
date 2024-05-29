class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        p1=0
        p2=0
        c={}
        s=0
        n=0
        while(p2<=len(nums)-1):

            if p2-p1<=k-1:

                if nums[p2] not in c.keys():
                    c[nums[p2]]=[p2]
                    s+=nums[p2]
                    p2+=1

                else:
                   # print(nums[p2],c[nums[p2]])
                    h=c[nums[p2]].pop()
                    c[nums[p2]]=[p2]  
                    #print(nums[p2],c[nums[p2]],p1,h)
                    if h>=p1:
                        s-=sum(nums[p1:h+1])
                        p1=h+1
                    p2+=1
                    s+=nums[p2-1]
                    #print(nums[p2],c[nums[p2]],p1,h)
   
                    if s<0:
                        s=0
            else:

                c[nums[p1]].pop(0)
                if c[nums[p1]]==[]:
                    c.pop(nums[p1])
                    s-=nums[p1]
                    if s<0:
                        s=0
                p1+=1


                if nums[p2] not in c.keys():
                    c[nums[p2]]=[p2]
                    s+=nums[p2]
                    p2+=1

                else:

                    h=c[nums[p2]].pop()
                    c[nums[p2]]=[p2]
                    if h>=p1:
                        s-=sum(nums[p1:h+1])
                        p1=h+1
                    p2+=1
                    s+=nums[p2-1]
                    s-=sum(nums[p1:h+1])
                    if s<0:
                        s=0

            if p2-p1==k:
                if s>n:
                    n=s

            



           # print(s,p1,p2,c)
        return n


            


            
        