class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        c={}
        t=[]
        for j in adjacentPairs:
            if j[0] in c.keys():
                    c[j[0]]+=[j[1]]
            else:
                    c[j[0]]=[j[1]]

            if j[1] in c.keys():
                    c[j[1]]+=[j[0]]
            else:
                    c[j[1]]=[j[0]]

              
        for k,v in c.items():

            if len(v)==1:
                r=k
                break

        

        t.append(r)
        y=c[r][0]
        c.pop(r)
        r=y
        
        while(len(c)!=0):
            t.append(r)
            
            for h in c[r]:
                if h in c.keys():
                    y=h
                    c.pop(r)
                    r=y

            if len(t)==len(adjacentPairs)+1:
                break
                    

        return t





        
        
            

                    

        
        