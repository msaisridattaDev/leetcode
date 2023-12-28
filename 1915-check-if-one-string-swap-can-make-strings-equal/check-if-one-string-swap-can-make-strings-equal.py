class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        t=[]

        if s1==s2:
            return True

        for i in range(len(s1)):

            if s1[i]==s2[i]:
                continue
            else:
                t+=[i]

        if len(t)==2:

            x,y=t
            print(x,y)
            if s1[y]+s1[x]==s2[x]+s2[y]:
                return True
        
        return False

        
        