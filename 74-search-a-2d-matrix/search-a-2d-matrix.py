class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        k=len(matrix)
        n=len(matrix[0])
        row=-1
        l=0
        h=k

        while((l<=k-1 and  h>=0) and l<=h):
            m=int((l+h)/2)
            print(m)
            if matrix[m][n-1] >= target >= matrix[m][0]:
                row=m
                break
            elif target > matrix[m][n-1]:
                l=m+1
            elif matrix[m][0] >  target:
                h=m-1

        if row==-1:
            return False
        
        l=0
        h=n

        while(l<=h ):
            m=int((l+h)/2)
            print(m)
            if matrix[row][m] < target:
                l=m+1
            elif target == matrix[row][m]:
                return True
            elif matrix[row][m] > target:
                h=m-1

        return False
        

