class Solution:
    def decodeString(self, s: str) -> str:

        k= list(s)
        q=[]
        k=[]
        for i in range(len(s)):

            if len(k)>0:

                if not s[i].isalpha() and s[i]!="[" and s[i]!="]":

                    if not k[-1].isalpha() and k[-1]!="[" and k[-1]!="]":
                        b=k.pop()
                        k.append(b+s[i])
                        #print(k)
                    else:
                        k.append(s[i])
                else:
                    k.append(s[i])
            else:
                k.append(s[i])
    
        for i in k:

            if i.isalnum():
    
                q.append(i)
            else:

               
                if i=="]":
                    w=""
                    f=False
               
                    p=q.pop()

                    #w+=p
                    ans=""
                    #print(p,i,q)
                    while not f and len(q)!=0:

                       # print(p)
                        if p=="[":
                            f=True
                        else:
                            if len(p)==1:
                                w+=p
                            else:
                                w+=p[::-1]

                        p=q.pop()

                   # print("after",p,w)
                    
                    if p.isalpha():
                        ans+=w[::-1]
                    else:
                        #print(p,w,w[::-1],ans)
                        w=w[::-1]
                        ans+=w*int(p)


                    #print("ans is",ans)
                    q.append(ans)
                    #print("ans is",ans,q)
                
                elif i=="[":
                    q.append(i)

                #print(q)
            
        #print(q)

        return "".join(q)




                    



                    






