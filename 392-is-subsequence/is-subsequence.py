class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        p1=0
        p2=0

        while(p1<=len(s)-1 and p2<= len(t)-1 ):

            if s[p1]==t[p2]:
                #print(p1,p2)
                p1+=1
                p2+=1
            else:
                p2+=1
           # print(p1,p2)

        if p1==len(s):
            return True
        return False
        