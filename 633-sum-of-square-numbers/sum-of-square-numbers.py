class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        l=[0]
        p=1
        i=1

        while(p<=c):
            p=i*i
            if p <=c:
                l.append(p)
            i+=1

        p1=0
        p2=len(l)-1

        print(l)
        while(p1<=p2):

            if l[p1]+l[p2]< c:
                p1+=1
            elif l[p1]+l[p2]> c:
                p2-=1
            else:
                return True

            