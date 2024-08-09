
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        m=len(board)
        n=len(board[0])

        
        options=[[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0]]

        for i in range(m):
            for j in range(n):
                count=0
                for h in options:
                    r,s=h
                    if 0<=i+r<=m-1 and  0<=j+s<=n-1:

                        if type(board[i+r][j+s])==int:
                            p=board[i+r][j+s]
                        else:
                            p,waste=board[i+r][j+s]
                        
                        if p==1:
                            count+=1
                
                if count<2:
                    prev=board[i][j]
                    board[i][j]=[prev,0]
                elif 2<=count<=3:
                    if board[i][j]==1:
                        prev=board[i][j]
                        board[i][j]=[prev,1]
                    else:
                        if count==3:
                            prev=board[i][j]
                            board[i][j]=[prev,1]
                elif count>3:
                    prev=board[i][j]
                    board[i][j]=[prev,0]

        i,j=0,0
        for i in range(m):
            for j in range(n):
                if type(board[i][j])==int:
                    ans=board[i][j]
                else:
                    waste,ans=board[i][j]

                board[i][j]=ans


                








        