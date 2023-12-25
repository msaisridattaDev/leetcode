class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=len(accounts)
        t=0
        p=0
        for i in range(m):
            t=sum(accounts[i])
            if t>=p:
                p=t  
        return p          
                

        