class Leaderboard:

    def __init__(self):
        self.c={}

    def addScore(self, playerId: int, score: int) -> None:
        
        if playerId in self.c.keys():
            self.c[playerId]+=score
        else:
            self.c[playerId]=score

        sorted(self.c.items(),key= lambda x:x[1])

    def top(self, K: int) -> int:
        
        f=list(sorted(self.c.items(),key= lambda x:x[1]))
        f.reverse()

        s=0
        #print(K)
        for j in range(K):
            if len(f)!=0:
                s+=f[j][1]
                
        return s


    def reset(self, playerId: int) -> None:
        
        if playerId in self.c.keys():
            self.c[playerId]=0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)