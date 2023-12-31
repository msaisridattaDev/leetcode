class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        c={}
        for i,v in enumerate(groupSizes):

            if v in c.keys():
                c[v]+=[i]
            else:
                c[v]=[i]
        
        #print(c)

        t=[]
        for  k,p in c.items():

            c= int(len(p)/k)
            
            q=0
            for j in range(c):
                t.append(p[q:q+k])
                q=q+k
            
        return t




        