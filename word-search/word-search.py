import itertools
class Solution:

    def check(self,board,word,i,j,wi,vis) -> bool:

        if wi>len(word)-1:
            return True
        
        u=[-1,1,0,0]
        s=[0,0,-1,1]
        x=False
        for r in range(4):
            if  0<=i+u[r] <= len(board)-1 and  0<= j+s[r] <= len(board[0])-1:
  
                if board[i+u[r]][j+s[r]]==word[wi] and [i+u[r],j+s[r]] not in vis:
                        x=True
                        vis+=[[i+u[r],j+s[r]]]
                        if self.check(board,word,i+u[r],j+s[r],wi+1,vis):
                            return True
                        else:
                            vis.pop()
                            continue
        if not x:
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        q=False
        g=len(board)
        f=len(board[0])
        vis=[]
        o=set(word)
        fl=set(list(itertools.chain(*board)))

        if o.difference(fl):
            return False

        for i in range(g):
            for j in range(f):
                if board[i][j]==word[0]:
                    if self.check(board,word,i,j,1,vis+[[i,j]]):
                        q=True
                        break
                    else:
    
                        pass
            if q:
                break

        if q:
            return True
        return False

        
        