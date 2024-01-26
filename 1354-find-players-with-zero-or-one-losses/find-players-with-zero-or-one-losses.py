class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        c={}
        for i in matches:
            
            if i[0] not in c.keys():
                c[i[0]]=0
            else:
                if c[i[0]]==1:
                    pass
                elif c[i[0]]>1:
                    pass

            if i[1] not in c.keys():
                c[i[1]]=1
            else:
                if c[i[1]]==1:
                    c[i[1]]=2 
                elif c[i[1]]==0:
                    c[i[1]]=1      
                elif c[i[1]]>1:
                    c[i[1]]+=1

        #print(c)

        r=[]
        t=[]

        for k,v in c.items():

            if v==1:
                t.append(k)
            elif v==0:
                r.append(k)

        r.sort()
        t.sort()
        return [r,t]


        



