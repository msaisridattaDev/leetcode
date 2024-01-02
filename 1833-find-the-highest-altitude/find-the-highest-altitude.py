class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        p=0
        m=0

        for i in gain:
            p+=i

            if p>=m:
                m=p

        return m