class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        v=set(word1).union(word2)
        
        t={}
        u={}
        for i in word1:
            if i in t.keys():
                t[i]+=1
            else:
                t[i]=1

        for j in word2:
            if j in u.keys():
                u[j]+=1
            else:
                u[j]=1

        for h in v:

            if h in t.keys() and  h in u.keys():
                if abs(t[h]-u[h]) <=3:
                    continue
                else:
                    return False
            elif h  in t.keys():

                if t[h]>3:
                    return False
            elif h  in u.keys():

                if u[h]>3:
                    return False
        return True

            