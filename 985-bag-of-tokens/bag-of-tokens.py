class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        p1=0
        p2=len(tokens)-1

        score=0

        while(p1<= p2):
            if power >= tokens[p1]:

                power-=tokens[p1]
                p1+=1
                score+=1
            else:
                if power < tokens[p2] and score > 0 and p1!=p2:
                    power+=tokens[p2]
                    score-=1
                    p2-=1
                else:
                    break

            #print(power,score,p1,p2)
    
        return score





        

