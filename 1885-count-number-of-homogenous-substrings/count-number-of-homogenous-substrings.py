class Solution:
    def countHomogenous(self, s: str) -> int:
        s+="&"
        print(len(s),set(s))
        p=s[0]
        m=[]
        k=[]
        for i in range(1,len(s)):
            if s[i] in p:
                p+=s[i]
            else:
                if len(p)>1:
                    c=len(p)

                    m+=[ int((c)*(c+1)/2)]
                else:
                    k+=[len(p)]
                p=""
                p=s[i]
            #print(p)
        print(m,k)

        return (sum(m)+sum(k))%(10**9+7)



        