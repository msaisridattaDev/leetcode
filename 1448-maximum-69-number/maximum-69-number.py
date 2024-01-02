class Solution:
    def maximum69Number (self, num: int) -> int:
        
        p=""
        num=str(num)
        c=0
        for i in num:

            if i=="9":
                p+=i
            else:
                if c==0:
                    p+="9"
                    c+=1
                else:
                    p+=i

        return int(p)
