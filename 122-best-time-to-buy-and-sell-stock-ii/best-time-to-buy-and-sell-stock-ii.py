class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        d=[0]*len(prices)
        d[0]=prices[0]

        for i in range(1,len(prices)):

            if prices[i] < d[i-1]:
                d[i]=prices[i]
            else:
                s+= prices[i]-d[i-1]
                d[i]=prices[i]

        return s
        