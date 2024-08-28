
#####3#########
import queue
class Solution:
     def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        q = queue.Queue()
        fresh_count = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 2:
                    q.put((i, j, 0))  
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        max_time = 0
        

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while not q.empty():
            i, j, time = q.get()
            max_time = max(max_time, time)
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh_count -= 1
                    q.put((ni, nj, time + 1))
        
        return max_time if fresh_count == 0 else -1

'''
    def countMin(self, grid,i,j,ans,N,M):

        q=queue.Queue()
        q.put((i,j))


        while not(q.empty()):

            i,j=q.get()
            #ans=ans+1
            temp=0
            u=[-1,1,0,0]
            p=[0,0,-1,1]
            max_ans=0

            for r in range(len(u)):
                if (i+u[r]<0 or j+p[r]<0 or i+u[r]>N-1 or j+p[r]>M-1):
                    pass
                else:
                   # print(i+u[r],j+p[r],"Val of",grid[i+u[r]][j+p[r]],"printing all n4s of",i,j)

                    if grid[i+u[r]][j+p[r]]==1:
                        grid[i+u[r]][j+p[r]]=2
                        q.put((i+u[r],j+p[r]))

                        temp=1
            if temp==1:
                max_ans=max_ans+1
                #print(ans,"with current",i,j)
        return max_ans
                    #self.countMin(grid,i+u[r],j+p[r],ans,N,M)



    def orangesRotting(self, grid: List[List[int]]) -> int:

        N=len(grid)
        M=len(grid[0])
        ans=0
        c=0
        for i in range(N):

            for j in range(M):
                if grid[i][j]==2:
                    ans=max(ans,self.countMin(grid,i,j,ans,N,M))
                    
        
        
        for i in range(N):

            if 1 in grid[i]:
                return -1

        return ans
'''
        