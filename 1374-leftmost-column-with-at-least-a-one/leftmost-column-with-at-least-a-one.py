# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
import sys
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m,n=binaryMatrix.dimensions()

        n=n-1
        m=m

        l=0
        h=n
        ans=-sys.maxsize

        flag=False
        while(l<=h):

            q= int((l+h)/2)
            

            for i in range(m):
                p=binaryMatrix.get(i,q)
        
                if p==1:
                    flag=True
                    break
               

            if flag:     
                ans=q
                h=q-1
                flag=False

            else:
                l=q+1

        
        if ans!=-sys.maxsize:
            return ans
        return -1


        