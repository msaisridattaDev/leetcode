import sys

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        w1=[]
        w2=[]
        ans=sys.maxsize


        for i,v in enumerate(wordsDict):

            if v==word1:
                w1+=[i]
            elif v==word2:
                w2+=[i]

        p1=0
        p2=0

        print(w1,w2)
        while(p1<=len(w1)-1 and p2<=len(w2)-1):

            if abs(w1[p1]-w2[p2])<ans:
                ans=abs(w1[p1]-w2[p2])

            if w1[p1]<w2[p2]:
                p1+=1
            else:
                p2+=1

        return ans       


