class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        r=len(matrix)
        c=len(matrix[0])
        t=[]
        for j in range(c):
            c=[]
            for i in range(r):
                c.append(matrix[i][j])

            t.append(c)

        return t

            