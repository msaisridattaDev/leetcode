import copy
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        h=copy.deepcopy(arr)
        
        c={}

        i=0
        while(i<=len(arr)-1):
            
            if arr[i] in c.keys():
                arr.pop(i) 
                i-=1
            else:
                c[arr[i]]=0

            i+=1

        print(arr)
        arr.sort()

        for i,v in enumerate(arr):
                c[v]=i

        t=[]

        for j in h:
            t.append(c[j]+1)


        return t 
        
