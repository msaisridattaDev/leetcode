import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        t={}
        r={}
        x=[]
        for j in words:
            if j in t.keys():
                t[j]+=1
            else:
                t[j]=1
    
        g=sorted(t.items(),key= lambda x:x[1], reverse=True)

        q=[]
        for b in g:
            if b[1] in r.keys():
                r[b[1]]+=[b[0]]
                
            else:
                r[b[1]]=[b[0]]

        
        
        for e in r.keys():
            q+=sorted(r[e])
        print(r,g,q)
        for w in range(k):
            x+=[q[w]]
        return x

        