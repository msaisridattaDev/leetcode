class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:


        c={}

        for i in nums:
            if i in c.keys():
                c[i]+=1
            else:
                c[i]=1

        p=list(c.items())
        p.sort()
        print(p)
        
        a=0
        for j in p:
            if j[0]+k in c.keys():
                #print(c[j[0]+k],c[j[0]],j[0],j[0]+k)
                a+=c[j[0]+k]*c[j[0]]

        return a
