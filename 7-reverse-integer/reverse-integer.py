class Solution:
    def reverse(self, x: int) -> int:
        f=str(x)
        if f[0]!="-":
            if int(f[::-1]) in range(-2**31, 2**31 - 1):
                return int(f[::-1])
            return 0
        else:
            if -int(f[-1:-len(f):-1]) in range(-2**31, 2**31 - 1):
                return -int(f[-1:-len(f):-1])
            return 0
        