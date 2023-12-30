import heapq,copy

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        c={}
        g=copy.deepcopy(score)
        h=len(score)
        heapq.heapify(score)
        while(len(score)!=0):

            p=heapq.heappop(score)

            c[p]=str(h)
            h-=1
            

        t=[]
       # print(g)
        for i in g:

            if c[i]=="1":
                t.append("Gold Medal")
            elif c[i]=="2":
                t.append("Silver Medal")
            elif c[i]=="3":
                t.append("Bronze Medal")
            else:
                t.append(c[i])

           # print(t)
        return t

        