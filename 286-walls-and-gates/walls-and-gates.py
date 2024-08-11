class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q=[]

        m=len(rooms)
        n=len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append((i,j))


        k=[[-1,0],[1,0],[0,-1],[0,1]]

        #print(q)

        while q:
            r,c=q.pop(0)
            for h in k:

                hr,hc=h


                if 0<=r+hr<=m-1 and 0<=c+hc<=n-1:
            
                    if rooms[r+hr][c+hc]==2147483647 and rooms[r+hr][c+hc]>rooms[r][c]+1:
                        rooms[r+hr][c+hc]=rooms[r][c]+1

                        q.append((r+hr,c+hc))


            
        