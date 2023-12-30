class Solution:
    def addDigits(self, num: int) -> int:
        def addDigits(num):
            
            print(num)
            if int(num/10)==0:
                return num

            s=str(num)
            p=0
            for i in s:
                p+=int(i)

            return addDigits(p)

        return addDigits(num)
            
