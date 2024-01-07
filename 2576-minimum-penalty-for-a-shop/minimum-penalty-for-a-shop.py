
import sys
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        s=customers

        psy=[0]

        psn=[0]

        for i in s:

            if i=="Y":
                psy.append(psy[-1]+1)
                psn.append(psn[-1])
            else:
                psn.append(psn[-1]+1)
                psy.append(psy[-1])

        

        m=sys.maxsize
        ans=-sys.maxsize
        for j in range(len(s)+1):

            w=psn[j]+psy[-1]-psy[j]
            

            if w<m:
                m=w
                ans=j

            #print(w,m,ans)

        return ans
        
        