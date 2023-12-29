class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        c={}
        t={}
        x=[]
        y=[]

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
            if h not in t.keys():
                x+=[h]

        for q in t.keys():
            if q not in c.keys():
                y+=[q]  

        
        return [x,y]

        