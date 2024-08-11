class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        ans=0
        def canEat(k):
            no_of_hours=0
            for p in piles:
                o=p/k
                if o > int(o):
                    no_of_hours+=int(o)+1
                else:
                    no_of_hours+=int(o)
           # print("no_of_hours are",no_of_hours,h)
            return no_of_hours<=h

        low=1
        high=max(piles)

        while(low<=high):

            m=int((low+high)/2)

            #print(m)
            if canEat(m):
               # print("yes",m)
                ans=m
                high=m-1
            else:
                #print("no",m)
                low=m+1

        return ans

            





