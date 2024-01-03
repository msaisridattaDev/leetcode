class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        c={}
        m=0
        for i,v in enumerate(nums):
            if v in c.keys():
                c[v]+=[i]
            else:
                c[v]=[i]
        
        for y in c.values():

            if m<=len(y):
                m=len(y)

        f=[]
        for g in range(m):
            f.append([])


        for m,n in c.items():

            for a in range(len(n)):
                f[a].append(m)

        return f




