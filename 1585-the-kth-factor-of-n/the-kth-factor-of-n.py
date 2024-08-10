class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        sqrtno=int(n**(0.5)+1)
        
        l=[]
        sl=[]

        for i in range(1,sqrtno+1):

            if n%i==0:
                l.append(i)

                if int(n/i)!=i:
                    sl.append(int(n/i))
        
        nums=list(set(l+sl))

        
        nums.sort()

        if k-1<=len(nums)-1:
            return nums[k-1]
        return -1


        