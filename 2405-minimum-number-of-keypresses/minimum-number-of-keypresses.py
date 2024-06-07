from collections import Counter
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c={}
        count=0
        value=1
        score=0
        i=1


        u=dict(Counter(s))
        u=sorted(u.items(),key= lambda item:item[1] )
        u.reverse()
        #print(u)

        for i in u:

            if count==9:
                count=0
                value+=1

            #print(i)
            score+= value* i[1]
                
            count+=1


        #print(c)
        return score


