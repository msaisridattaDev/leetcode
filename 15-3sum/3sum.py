class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        d=sorted(nums)

        m=[]

        while(len(d)!=0):
            u=len(d)-1
            c=-(d.pop(-1))
            p1=0
            p2=len(d)-1

            while(p1<p2):

                s=d[p1]+d[p2]

                if s==c:
                    h=[d[p1],d[p2],-(c)]
                    if h not in m:
                        m+=[h]
                    p2-=1
                    p1+=1

                else:
                    if d[p2]>= c-d[p1] >= d[p1]:
                        p2-=1
                    else:
                        p1+=1

        return m
        


        