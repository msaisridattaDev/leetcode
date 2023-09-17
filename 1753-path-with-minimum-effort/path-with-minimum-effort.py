import sys
import heapq
import copy
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
 

        heights1 =copy.deepcopy(heights)
        row=len(heights)
        column=len(heights[0])
        p=row*column
        #src=[0][0]
        #dest=[row-1][column-1]
        dist=heights1
        g={}
        for m in range(row):
            for n in range(column):
                dist[m][n]=sys.maxsize
                k=(m,n)
                g[k]=[]
                for p in [-1,1]:
                    if m+p>=0 and  m+p<=row-1:
                        g[k]+=[[m+p,n]]
                    if n+p<=column-1 and n+p>=0:
                        g[k]+=[[m,n+p]]
        dist[0][0]=0
        queue=[(0,(0,0))]

      
        while len(queue)!=0:

            distance,node =heapq.heappop(queue)

            i,j=node

            for b in g[node]:

                cr,cc= b[0],b[1]

                distance2 =max(distance, abs(heights[i][j]- heights[cr][cc]))
 
                if distance2 < dist[cr][cc] :
                    dist[cr][cc]= distance2
 
                    heapq.heappush(queue,(distance2, (cr,cc)))

        return dist[row-1][column-1]
    
           
           

       


    
    
        

        
