class Solution:
    def maxLength(self, arr: List[str]) -> int:

        t=[]

    
        def maxLength(arr,l,i):

            global e

            if i>=len(arr):
                t.append(len(l))
                return

            if len(set(l).intersection(set(arr[i])))==0 and len(set(arr[i]))==len(arr[i]):
                maxLength(arr,l+arr[i],i+1)

            
            maxLength(arr,l,i+1)

        maxLength(arr,"",0)


        return max(t)
        