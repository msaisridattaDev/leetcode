class Solution:
    def firstUniqChar(self, s: str) -> int:

        c={}

        for i in range(len(s)):
            if s[i] in c.keys():
                c[s[i]][0]=c[s[i]][0]+1
            else:
                c[s[i]]=[1,i]

        b=sorted(c.values())

        if b[0][0]==1:
            return b[0][-1]
        else:
            return -1


        

        