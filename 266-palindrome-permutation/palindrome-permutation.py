class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        c={}

        for i in s:

            if i in c.keys():
                c[i]+=1
            else:
                c[i]=1

        v=list(c.values())

        e=0
        o=0

        for j in v:

            if j%2==0:
                e+=1
            else:
                o+=1

        if len(v)==e or (len(v)-1==e and o==1):
            return True