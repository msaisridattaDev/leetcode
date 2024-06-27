class Solution:
    def myAtoi(self, s: str) -> int:

        leading_space=False

        negative_sign=False

        positive_sign=False

        number_started=False
        sign=False

        w=""

        for i in s:

            if i=="0" or i in ["1","2","3","4","5","6","7","8","9"]:
                number_started=True
                w+=i
               # print(w)

            elif i==" " and not number_started and not sign:
                leading_space=True
                continue
            elif (i=="-" or i=="+") and not number_started and not sign:
                if i=="+":
                    positive_sign=True
                    sign=True
                else:
                    negative_sign=True
                    sign=True
                continue
            else:
                break

       # print(w,negative_sign,set(w))



        if len(set(w))>1:
            #print("yes",w)
            w=w.lstrip("0")


        if positive_sign and  negative_sign:
            return 0
        if w!="":
            #print(int(w))
            if negative_sign:
                if -int(w) < -2147483648:
                    return -2147483648
                else: 
                    return -int(w)
            else:
                if int(w) > 2147483647:
                    print("yes")
                    return 2147483647
                else: 
                    return int(w)

                
        else:
            return 0
            
            

