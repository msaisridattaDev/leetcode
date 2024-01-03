class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        p1=0
        p2=0

        while(p1<=len(g)-1 and p2<=len(s)-1):

            if s[p2]>=g[p1]:
                p2+=1
                p1+=1
            else:
                p2+=1

        return p1