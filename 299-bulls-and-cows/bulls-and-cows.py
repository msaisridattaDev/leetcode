class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        p=list(secret)
        q=list(guess)
        c={}
        b={}


        for i,v in enumerate(p):

            if v in c.keys():
                c[v]+=[i]

            else:
                c[v]=[i]

        for r,s in enumerate(q):

            if s in b.keys():
                b[s]+=[r]

            else:
                b[s]=[r]

        #print(c,b)

        x=0
        y=0
        



        t=list(c.keys())


        for g in t:

            if g in b.keys():
                
                p1=0
                p2=0

                while(p1<=len(c[g])-1 and p2<=len(b[g])-1):
                    
                    if c[g][p1]==b[g][p2]:
                        x+=1
                        #print(p1,p2)
                        c[g].pop(p1)
                        b[g].pop(p2)
                        #p1+=1
                        #p2+=1

                    elif c[g][p1] < b[g][p2]:
                        p1+=1
                        

                    elif c[g][p1] > b[g][p2]:
                        p2+=1
                        
                if len(b[g]) >= len(c[g]):
                    y+=len(c[g])
                elif len(b[g]) < len(c[g]):
                    y+=len(b[g])
       # print(x,y)
                

        return str(x)+"A"+str(y)+"B"