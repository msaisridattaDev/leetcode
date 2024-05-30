class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        c={}
        n=0

    

        for i,v in enumerate(citations):

            if v in c.keys():
                c[v]+=[i]
            else:
                c[v]=[i]

        

        q=[list(y) for y in c.items()]
        q.sort()
        q=q[::-1]



        q[0][1]=len(q[0][1])

        for r,s in enumerate(q):

            if r>0:
                q[r][1]=len(q[r][1])+q[r-1][0]

            q[r][0],q[r][1]=q[r][1],q[r][0]

        
        print(q)
        for h in q:

            if h[0]<=h[1]:
                if n < h[0]: 
                    n=h[0]

            else:
                if n < min(h[0],h[1]):
                    n=min(h[0],h[1])
                
        
        return n
    
 