class Solution:
    def countAndSay(self, n: int) -> str:
        
        def countAndSay(n,c,b) -> str:

            if b==n-1:
                return c
            
            #print(c,b)
            p=0
            a=c[0]
            w=0
            t=""
            while(p<=len(c)-1):

                #print(c[p],a,w,p)
                if c[p]==a:
                    w+=1

                else:
                    t+=str(w)+a
                    a=c[p]
                    w=1

                p+=1
            #print(t)

            return countAndSay(n,t+"&",b+1)

        v=countAndSay(n,"1&",0)
       # print(v)
        return v[:-1]

        

        
                


