class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend==0:
            return 0


        q=0
        m=1
        ngsign=False
        if dividend <0 and divisor <0:
            ngsign=False
        elif dividend <0 or divisor <0:
            ngsign=True
        
        dividend = abs(dividend)
        temp,divisor = abs(divisor),abs(divisor)

        
        while dividend>=divisor:

            while dividend>=(divisor<<1):

                divisor= divisor<<1
                m= m<<1

        
            dividend-=divisor
            q+=m
            m=1
            divisor=temp

        if ngsign:
            return - min(q,min(q,2147483648))
        return min(q,min(q,2147483647))

        


