class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        d={}
        n=len(graph)-1
    

        res={}
        def allPathsSourceTarget2(graph,j,l):


            d[j]=[]

            for i in graph[j]:
                #print(i)

                if i==n:
                    if j!=0:
                        l+=[i]
                        d[j]+=[l]
                    else:
                        l+=[i]

                        d[j]+=[l]
                        
                else:
                    #print("yes")

                    if i not in d.keys():
                        #print("yes")
                        p=allPathsSourceTarget2(graph,i,[i])
                       # print("p is",p,j)
                        for h in p:

                            d[j]+=[[j]+h]
                        
                    else:
                        if d[i]!=None:
                           # print(d[i])
                            for h in d[i]:
                               # print(h,j)
                                d[j]+=[[j]+h]

            #print(d)

            return d[j]

        v=allPathsSourceTarget2(graph,0,[0])
        
        return v
                    
    

                    
                        
                        
                    

                        
                


        allPathsSourceTarget2(graph,0,[0])


                    


                