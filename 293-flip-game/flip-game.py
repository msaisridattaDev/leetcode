class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        

        p=0
        p1=1
        t=[]
        while(p1<=len(currentState)-1):

            if currentState[p]=="+" and currentState[p1]=="+":
                t.append(currentState[0:p]+"--"+currentState[p1+1::])

            p+=1
            p1+=1
        return t






        