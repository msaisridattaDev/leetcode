class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        row=len(matrix)
        column=len(matrix[0])
        t=row*column
        f=t-k
        l=[]
        h={}
        h[(row-1,column-1)]=matrix[row-1][column-1]
        v=[[matrix[row-1][column-1],(row-1,column-1)]]
        l+=[matrix[row-1][column-1]]

        for i in range(f+1):
            heapq._heapify_max(v)
            rj,ri =heapq._heappop_max(v)
            p=-1
    #print(rj)
            c1=(ri[0]+p,ri[1])
            c2=(ri[0],ri[1]+p)
            m=rj
            if  row-1 >= c1[0]>= 0  and  column-1 >= c1[1]>= 0 :
                if c1 not in h.keys():
                    h[(c1[0],c1[1])]=matrix[c1[0]][c1[1]]
                    v+=[[matrix [c1[0]][c1[1]],(c1[0],c1[1])]]
            if  row-1 >= c2[0]>= 0  and  column-1 >= c2[1]>= 0 :
                if c2 not in  h.keys():
                    h[(c2[0],c2[1])]=matrix [c2[0]][c2[1]]
                    v+=[[matrix [c2[0]][c2[1]],(c2[0],c2[1])]]

        return m
        