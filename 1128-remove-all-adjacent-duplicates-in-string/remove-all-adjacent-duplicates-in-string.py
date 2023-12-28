class Solution:
    def removeDuplicates(self, s: str) -> str:

        p1=0
        p2=1

        q=list(s)
        while( p2<=len(q)-1):
            #print(p1,p2)
            if q[p1]==q[p2]:
                q.pop(p2)
                q.pop(p1)
                if p1!=0 and p2!=0:
                    p1-=1
                    p2-=1
            else:
                p1+=1
                p2+=1

        print(q)

        return "".join(q)



        