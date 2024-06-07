class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        d={}

        def minPathSum(i,j):

            d[(i,j)]=0

            if i==m-1 and j==n-1:
                d[(i,j)]=1

                return d[(i,j)]
            

            p=[[1,0],[0,1]]

            for h in p:

                if i+h[0]<= m-1 and j+h[1] <= n-1:
                    if(i+h[0],j+h[1]) not in  d.keys():
                        p=minPathSum(i+h[0],j+h[1])
                        d[(i,j)]+= p

 
                    else:
                        d[(i,j)]+= d[(i+h[0],j+h[1])]
                         

            return d[(i,j)]
                
    
        u=minPathSum(0,0)
    
        return u


