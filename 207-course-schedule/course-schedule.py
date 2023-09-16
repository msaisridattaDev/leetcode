class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        zi=[]
        g={}
        u=[0]*(numCourses)
        
     

        for i in prerequisites:
            if i[1] in g.keys():
                g[i[1]]=g[i[1]]+[i[0]]
            else:
                g[i[1]]=[]
                g[i[1]]=g[i[1]]+[i[0]]
       #y=l-v
        for j in g.items():
            #print(j)
            for x in j[1]:
                u[x]+=1
            

        for i in range(len(u)):
            if u[i]==0:
                zi+=[i]

        y=[]
        while len(zi)!=0:
            c=zi.pop(0)
            y+=[c]
            #print(g,g[c])
            try:
                for t in g[c]:
                    u[t]-=1
                    if u[t]==0:
                        zi+=[t]
                        y+=[zi]
            except:
                pass

        print(g.items(),y)
        for m in range(0,numCourses):

            if m not in y:
                return False
        return True

           

     
