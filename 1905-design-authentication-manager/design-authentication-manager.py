class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.t=timeToLive
        self.d={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        
        self.d[tokenId]=currentTime+self.t

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.d.keys():
            
            if currentTime<self.d[tokenId]:
                self.d[tokenId]=currentTime+self.t


    def countUnexpiredTokens(self, currentTime: int) -> int:

        v=list(self.d.values())
        
        w=0
        for i in v:
            #print(i,self.d,currentTime)
            if i > currentTime:
                w+=1
        #print(self.d,v,currentTime,w)
        return w

            


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)