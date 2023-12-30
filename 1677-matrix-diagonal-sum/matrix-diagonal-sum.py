class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        s=0
        n=len(mat)
        for i in range(n):

            s+=mat[i][i]
            s+=mat[i][(n-1)-i]

        if n%2==0:
            return s
        else:
            k=int(n/2)
            return s-mat[k][k] 


