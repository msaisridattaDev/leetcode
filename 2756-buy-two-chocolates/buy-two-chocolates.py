class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        f=min(prices)
        prices.remove(f)
        s=min(prices)

        if money-(f+s) >=0:
            return money-(f+s)
        else:
            return money
        