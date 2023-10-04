class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        y=sorted(people)
        print(y)
        p1=0
        p2=len(y)-1
        c=0
        flag=0
        while(p1<=p2):

            if y[p1]+y[p2] > limit:
                p2-=1
                c+=1
            else:
                p1+=1
                p2-=1
                c+=1

        return c


        