import sys
class Solution:
    def maxScore(self, s: str) -> int:
        
        w=[int(s[0])]
        ans=-sys.maxsize
        
        for i in range(1,len(s)):
            w.append(int(w[-1])+int(s[i]))

        
        print(w)
        p1=0
        p2=len(w)-1

        while(p1<p2):



            c=w[p2]-w[p1]+len(w[0:p1+1])-w[p1]

            #print(len(w[0:p1+1])-int(w[p1]),(int(w[p2])-int(w[p1])),c)

            if ans < c:
                ans=c
            p1+=1

        return ans



