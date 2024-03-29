# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        h=n
        l=1

        while(l<=h):

            m=int((l+h)/2)

            if guess(m) <0:
                h=m-1
            elif guess(m)==0:
                return m
            elif guess(m)>0:
                l=m+1
        