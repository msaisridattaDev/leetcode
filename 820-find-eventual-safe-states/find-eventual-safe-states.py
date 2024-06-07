class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        zi=[]
        g={}
        u=[0]*(len(graph))
    
        

        for i,v in enumerate(graph):

            for t in v:
                if t in g.keys():
                    g[t]+=[i]
                else:
                    g[t]=[i]

       
        for j in g.items():
            #print(j)
            for x in j[1]:
                u[x]+=1
        #print(g,u)

        for i in range(len(u)):
            if u[i]==0:
                zi+=[i]

        #print(zi)

        y=[]
        while len(zi)!=0:
            c=zi.pop(0)

            y+=[c]
            #print(g,g[c])
            try:
                for b in g[c]:
                    u[b]-=1
                    if u[b]==0:
                        zi+=[b]
            
            except:
                pass

    
            
        y.sort()
        return y