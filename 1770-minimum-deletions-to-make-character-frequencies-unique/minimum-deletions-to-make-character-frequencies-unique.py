class Solution:
    def minDeletions(self, s: str) -> int:
        t={}

        for i in range(len(s)):
            if s[i] in t.keys():
                t[s[i]]+=1
            else:
                t[s[i]]=1
        #print(t)
        #d= sorted(t.items(), key= lambda x:x[1])

        d=list(t.values())
        d.sort()
       # print(d)

        y={}

        for j in d:
            if j in y.keys():
                y[j]+=1
            else:
                y[j]=1

       # print(y)

        w=0

        for h in range(len(d)):

            if d[h] in y.keys() and y[d[h]]==1:
                pass
            else:
                u=d[h]
                while(y[u]>1):
                    d[h]=u
                    while(1):
                       # print(d[h],w,y[u])
                        d[h]-=1
                        w+=1
                        if d[h]==0 or d[h] not in y.keys():
                            y[d[h]]=1
                           # print(y,d[h])
                            break

                    y[u]-=1


        return w
        