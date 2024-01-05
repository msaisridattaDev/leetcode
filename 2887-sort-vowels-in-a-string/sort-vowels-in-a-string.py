class Solution:
    def sortVowels(self, s: str) -> str:

        p=""

        for i in s:
            if i in "AEIOUaeiou":
                p+=i

        f=sorted(p)

        p1=0

        t=""

        for j in s:

            if j not in "AEIOUaeiou":
                t+=j
            else:
                if p1<=len(f)-1:
                    t+=f[p1]
                    p1+=1
        
        return t
        
        