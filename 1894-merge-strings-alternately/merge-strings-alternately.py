class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        c=0
        p1=0
        p2=0
        s=""
        while(p1<=len(word1)-1 and p2<=len(word2)-1):

            if c%2==0:
                s+=word1[p1]
                p1+=1
            else:
                s+=word2[p2]
                p2+=1
            c+=1

        if p1==len(word1):
            s+=word2[p2::]
        else:
            s+=word1[p1::]

        
        return s


        