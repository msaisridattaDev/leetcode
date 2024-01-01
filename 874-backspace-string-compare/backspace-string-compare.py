class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        p=""
        q=""
        for i in s:

            if i=="#":
                if len(p)!=0:
                    p=p[:-1]
            else:
                p+=i

        for j in t:

            if j=="#":
                if len(q)!=0:
                    q=q[:-1]
            else:
                q+=j

        return p==q
