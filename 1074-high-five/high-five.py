import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        c={}

        for i in items:

            if i[0] in c.keys():
                c[i[0]].append(i[1])
            else:
                c[i[0]]=[i[1]]

        r=[]
        d=list(c.keys())
        d.sort()
        for j in d:

            heapq.heapify(c[j])

            for k in range(5):
                s=heapq.nlargest(5,c[j])
            
            p=int(sum(s)/5)

            r.append([j,p])

        
        return r

    

