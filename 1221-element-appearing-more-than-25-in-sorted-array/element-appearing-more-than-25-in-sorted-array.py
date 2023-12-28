class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        mc=0
        rc=0
        arr.append(-1)
        for i in range(1,len(arr)):

            if arr[i]==arr[i-1]:
                rc+=1

            else:
                if rc>=mc:
                    print(mc,rc)
                    mc=rc
                    ans=arr[i-1]
                rc=0
                    

        return ans