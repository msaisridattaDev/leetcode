class BrowserHistory:

    def __init__(self, homepage: str):

        self.l=[]
        self.l.append(homepage)
        self.p=0
        
    def visit(self, url: str) -> None:


        self.l=self.l[0:self.p+1]
        self.l.append(url)
        self.p+=1

        

    def back(self, steps: int) -> str:

        
        while(steps>0  and self.p>0):
            self.p-=1
            steps-=1
        return self.l[self.p]

    def forward(self, steps: int) -> str:
        while(steps>0  and self.p<len(self.l)-1):
            self.p+=1
            steps-=1
        return self.l[self.p]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)