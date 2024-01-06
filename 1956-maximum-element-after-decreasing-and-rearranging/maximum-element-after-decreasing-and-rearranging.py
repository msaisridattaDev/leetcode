class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        arr[0]=1
        for j in range(len(arr)-1):

            if arr[j+1]-arr[j]==1 or arr[j+1]-arr[j]==0 :
                pass
            else:
                arr[j+1]=arr[j]+1
            
        #print(arr)

        return arr[-1]
