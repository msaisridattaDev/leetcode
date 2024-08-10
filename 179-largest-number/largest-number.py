from functools import cmp_to_key

def func1(a,b):

    if a+b > b+a:
        return -1
    elif a+b < b+a:
        return 1
    else:
        return 0

key1=cmp_to_key(func1)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums=list(map(str,nums))

        nums.sort(key=key1)


        p= "".join(nums)

        if int(p)==0:
            return "0"
        return p


