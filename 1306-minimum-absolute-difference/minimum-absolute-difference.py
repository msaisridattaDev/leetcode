class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        t=[]
        for i in range(1,len(arr)):
            t.append(arr[i]-arr[i-1])

        
        v=min(t)
        p=[]
        for j in range(len(t)):

            if t[j]==v:
                p.append([arr[j],arr[j+1]])

        return p

