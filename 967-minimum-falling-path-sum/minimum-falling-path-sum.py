
import sys
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        d={}
        m=len(matrix)
        n=len(matrix[0])

        def minPathSum(matrix,i,j):

            d[(i,j)]= sys.maxsize

        

            if i==m-1:
                d[(i,j)]=matrix[i][j]

                return d[(i,j)]
            

            p=[[1,0],[1,1],[1,-1]]

            for h in p:

               

                if 0<=i+h[0]<= m-1 and 0<=j+h[1] <= n-1:
                    if(i+h[0],j+h[1]) not in  d.keys():
                        p=minPathSum(matrix,i+h[0],j+h[1])
                       
                      
                        if p+ matrix[i][j] < d[(i,j)]:
                           
                            d[(i,j)]= p+matrix[i][j] 

            
                    else:

                        if d[(i+h[0],j+h[1])] + matrix[i][j]  < d[(i,j)]:

                            d[(i,j)]= d[(i+h[0],j+h[1])]+matrix[i][j] 

                            
                         

            return d[(i,j)]
                
        for j in range(n):
            minPathSum(matrix,0,j)


        q=sys.maxsize
        for x in range(n):

            if d[(0,x)]<q:
                q=d[(0,x)]

        return q