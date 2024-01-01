class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        c= max(candies)

        t=[]

        for i in candies:
            t.append(i+extraCandies >=c)

        return t