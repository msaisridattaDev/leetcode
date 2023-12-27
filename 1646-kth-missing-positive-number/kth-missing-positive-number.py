class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        d=list(range(1,arr[-1]+k+1))

        #print(d)

        x= list(set(d)-set(arr))

        x.sort()

        return x[k-1]
        