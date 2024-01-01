class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        c={}

        for i in sentence:
           if i in c.keys():
               c[i]+=1
           else:
               c[i]=1

        t="abcdefghijklmnopqrstuvwxyz"

        p=0
        for j in t:

            if j in c.keys():
                p+=1
            else:
                return False

        return p==26
