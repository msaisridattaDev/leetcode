
import sys
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        d={}
        m=len(grid)
        n=len(grid[0])

        def minPathSum(grid,i,j):

            d[(i,j)]= sys.maxsize

        

            if i==m-1 and j==n-1:
                d[(i,j)]=grid[i][j]

                return d[(i,j)]
            

            p=[[0,1],[1,0]]

            for h in p:

                if i+h[0]<= m-1 and j+h[1] <= n-1:
                    if(i+h[0],j+h[1]) not in  d.keys():
                        p=minPathSum(grid,i+h[0],j+h[1])

                        if p+ grid[i][j] < d[(i,j)]:
                            d[(i,j)]= p+grid[i][j] 
                        

                    else:
                        if d[(i+h[0],j+h[1])] +1 < d[(i,j)]:

                            d[(i,j)]= d[(i+h[0],j+h[1])]+grid[i][j]  
                         

            return d[(i,j)]
                
    
        return minPathSum(grid,0,0)

