class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        v=piles
        v.reverse()
        print(v)
        s=0
        j=1
        p=v[j]

        for i in range(int(len(piles)/3)):
            print(p,j)
            s+=p
            if j+2<=len(v)-1:
                p=v[j+2]
                j+=2
        
        return s

