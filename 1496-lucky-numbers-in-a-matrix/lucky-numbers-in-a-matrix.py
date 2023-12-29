class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r=len(matrix)
        c=len(matrix[0])
        t=[]
        rws=[]
        cns=[]
        for j in range(c):
            c=[]
            for i in range(r):
                c.append(matrix[i][j])
            
                rws.append(min(matrix[i]))
            cns.append(max(c))
            t.append(c)

        #print(rws,cns)

        return set(rws).intersection(set(cns))

        
        