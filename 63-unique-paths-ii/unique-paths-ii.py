class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        d={}
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        def minPathSum(i,j):

            if obstacleGrid[i][j]==1:
                d[(i,j)]=0
                return -1

            d[(i,j)]=0

            if i==m-1 and j==n-1:
                d[(i,j)]=1

                return d[(i,j)]
            

            p=[[1,0],[0,1]]

            for h in p:

                if i+h[0]<= m-1 and j+h[1] <= n-1:
                    if(i+h[0],j+h[1]) not in  d.keys():
                        p=minPathSum(i+h[0],j+h[1])

                        if p==-1:
                            pass
                        else:
                            d[(i,j)]+= p
                        
 
                    else:

                        if d[(i+h[0],j+h[1])] == 0:
                            pass
                        else:
                            d[(i,j)]+= d[(i+h[0],j+h[1])]

            
                         

            return d[(i,j)]
                
    
        minPathSum(0,0)
    
        return d[(0,0)]
        
        