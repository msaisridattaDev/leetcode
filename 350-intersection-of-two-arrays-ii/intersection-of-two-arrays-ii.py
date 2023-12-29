class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        c={}
        t={}
        x=[]

        for i in nums1:
            if i in c.keys():
                c[i]+=1
            else:
                c[i]=1


        for j in nums2:
            if j in t.keys():
                t[j]+=1
            else:
                t[j]=1

        for h in c.keys():
            if h in t.keys():
                for v in range(min(c[h],t[h])):
                    x+=[h]

        
        return x


              