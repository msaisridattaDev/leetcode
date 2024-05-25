class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        c={}
        
        if not trust and n==1:
            return 1

        for i,v in enumerate(trust):

            if v[1] in c.keys():
                c[v[1]]+=[v[0]]
            else:
                c[v[1]]=[v[0]]

        print(c)
        ans=0
        for j in c.keys():

            if len(c[j])==n-1:
                ans=j
                
                for h in trust:
                    if j==h[0]:
                        return -1

        if ans!=0:
            return ans
        return -1