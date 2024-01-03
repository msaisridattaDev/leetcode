class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        p=""
        m=0
        c=0
        v="aeiou"
        for j in range(len(s)):

           # print(p,)
            if s[j] in v:
                c+=1

            if len(p)==k:

                if p[0] in v:
                    c-=1
                p=p[1::]
                p+=s[j]
            else:
                p+=s[j]

            if c>m:
                m=c

        return m