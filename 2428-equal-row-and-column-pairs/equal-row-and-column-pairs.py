class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        rows=[]
        columns=[]
        c={}
        count=0
        for h in range(n):
            rows.append("")
            columns.append("")
        

        for i in range(n):
            for j in range(n):
                p=str(grid[i][j])

                rows[i]+="-"+p
                columns[j]+="-"+p

        print(rows,columns)
        h=0
        for h in range(n):
            if rows[h] in c.keys():
                c[rows[h]]+=1
            else:
                c[rows[h]]=1

        print(count)
        for k in range(n):
            if columns[k] in c.keys():
                count+=c[columns[k]]
                
            print(count)

        return count

        




        