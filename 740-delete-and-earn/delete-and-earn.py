class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        c={}
        for i in nums:
            if i in c.keys():
                c[i]+=i
            else:
                c[i]=i
        r=list(set(nums))
        r.sort()
        d=[0]*len(r)
        d[0]=c[r[0]]

        #print(r)

        if len(r)>1:
            if r[1]-r[0]>1:
                d[1]=d[0]+c[r[1]]
            else:
                #print("yes")
                d[1]=max(d[0],c[r[1]])
                print(d[1])
            

        for i in range(2,len(r)):

            if r[i]-r[i-1]>1:
                d[i]=d[i-1]+c[r[i]]
            else:
                d[i]=max(d[i-2]+c[r[i]],d[i-1])
        

        #print(r,d)
        return d[-1]
        