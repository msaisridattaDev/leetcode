class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]

        for i in range(1,numRows):
            t=[]
            for j in range(0,i+1):

                if j-1>=0 and j<len(l[i-1]):
                    p=l[i-1][j-1]+l[i-1][j]
                else:
                    if j-1<0:
                        p=0+l[i-1][j]
                    elif j>=len(l[i-1]):
                        p=l[i-1][j-1]+0

                t.append(p)
            l.append(t)

        return l
                    
                

