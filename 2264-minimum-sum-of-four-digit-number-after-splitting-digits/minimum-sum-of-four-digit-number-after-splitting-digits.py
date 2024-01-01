class Solution:
    def minimumSum(self, num: int) -> int:

        s=str(num)
        l=[int(s[0]),int(s[1]),int(s[2]),int(s[3])]

        l.sort()

        return int(str(l[0])+str(l[2])) + int(str(l[1])+str(l[3]))

        

        


        