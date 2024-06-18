import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        c={}

        for j,v in enumerate(difficulty):

            if v in c.keys():
                if c[v]<profit[j]:
                    c[v]=profit[j]
            else:
                c[v]=profit[j]

        profit=[]

        difficulty.sort()

        for h in difficulty:

            profit.append(c[h])

        #print(profit,difficulty)

        s=0

        for g in worker:

            p=bisect.bisect_right(difficulty,g)

            if p==0:
                s+=0
            else:
                s+=max(profit[0:p])

        return s



        

        