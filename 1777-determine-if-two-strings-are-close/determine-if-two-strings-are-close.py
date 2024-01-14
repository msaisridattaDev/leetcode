class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        c={}
        b={}

        for i in word1:
            if i  in c.keys():
                c[i]+=1
            else:
                c[i]=1

        for j in word2:
            if j  in b.keys():
                b[j]+=1
            else:
                b[j]=1

        if sorted(c.keys())==sorted(b.keys())and sorted(c.values())==sorted(b.values()):
            return True

