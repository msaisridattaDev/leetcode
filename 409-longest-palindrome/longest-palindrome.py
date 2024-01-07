class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        c={}

        for i in s:
            if i in c.keys():
                c[i]+=1
            else:
                c[i]=1

        v=list(c.values())

        v.sort()
        print(v)

        e=0
        o=0
        w=0

        for j in v:

            if j%2==0:
                e+=j
            else:
                
                o+=j-1
                w+=1

        if w>0:
            return e+o+1

        return e+o
