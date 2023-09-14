class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        t={}
        for i in arr:
            if i in t.keys():
                t[i]+=1
            else:
                t[i]=1

        d=sorted(t.items(), key= lambda x:x[1])
        print(d,t)
        p=0
        h=0
        for j in range(1,k+1):
            if h < j:
                h+=d[p][1]
            if h==j:
                p+=1    
            print(h,j,k+1,p)
        return len(d)-(p)
