class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        m=len(grid)
        n=len(grid[0])
        v=False

        #print(m,n)
        d={}
        p=[[0,1],[-1,0],[0,-1],[1,0]]
        q=[]

        for i in range(m):
            for j in range(n):

                if grid[i][j]=="*":
                    d[(i,j)]=True
                
                    #print("yes",i,j)
                    for h in p:

                        if 0<=i+h[0]<=m-1 and 0<=j+h[1]<=n-1:

                            if grid[i+h[0]][j+h[1]]=="O":
                                #print("ÿes added",grid[i+h[0]][j+h[1]])
                                q.append((i+h[0],j+h[1]))
                            elif grid[i+h[0]][j+h[1]]=="#":
                                level=1
                                return level



                    v=True
                    break
                    
            if v:
                break

        v=False

       # print(q)


        level=0
        i,j=0,0

        while (len(q)!=0):

            l=len(q)
            level+=1

            for k in range(l):
                i,j=q.pop(0)

                if i<=m-1 and j<=n-1:

                    if (i,j) not in d.keys():
                        d[(i,j)]=True

                        if grid[i][j]=="#":
                            v=True
                            break
                        for h in p:

                            if 0<=i+h[0]<=m-1 and 0<=j+h[1]<=n-1:


                                if (i+h[0],j+h[1]) not in d.keys():

                                    if grid[i+h[0]][j+h[1]]=="O" or grid[i+h[0]][j+h[1]]=="#" :
                                            q.append((i+h[0],j+h[1]))

            if v:
                break

       # print(level)

        if v:
            return level
        else:
            return -1

                

                        
                    



        return 3
            
