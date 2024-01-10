import sys
sys.set_int_max_str_digits(0)

class Solution:
    def largestOddNumber(self, num: str) -> str:

        p=""
        m=""
        

        for i in num:
            p+=i

            if int(i)%2!=0:
                m=p

        return m