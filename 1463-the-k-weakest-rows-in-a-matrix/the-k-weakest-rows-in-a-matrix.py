class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        m=[]
        for i in range(len(mat)):

            m.append([sum(mat[i]),i])

        m.sort()
        t=[]
        for j in range(k):
            t.append(m[j][1])

        return t


            

