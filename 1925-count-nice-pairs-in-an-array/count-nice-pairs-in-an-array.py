class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        c = Counter()
        MOD = 1000000007
        
        for num in nums:
            p = str(num)
            f = int(p[::-1]) - num
            c[f] += 1

        w = 0
        for count in c.values():
            if count > 1:
                w += count * (count - 1) // 2
        
        return w % MOD








'''
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        c=Counter()
        for i in nums:
            p=str(i)
            v=p[::-1]
        
            f=int(p[::-1])-int(p)

            
            c[f]+=1
           


        w=0
        for count in c.values():
            if count > 1:
                w += count * (count - 1) // 2

        return w%10000000007

'''
                
        