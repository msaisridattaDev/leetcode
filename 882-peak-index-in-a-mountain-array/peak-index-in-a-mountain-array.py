class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l=0
        h=len(arr)

        while(l<=h):
            m=int((l+h)/2)

            print(l,h,m)
            if arr[m-1]< arr[m] and arr[m] > arr[m+1]:
                return m
            elif m+1<= len(arr)-1 and arr[m+1]< arr[m]:
                h=m-1
            elif m+1<= len(arr)-1 and arr[m+1] > arr[m]:
                l=m+1
            elif m==len(arr)-1:
                if arr[m-1]> arr[m]: 
                    h=m-1

            