class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        t={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        s=[]
        carry=0
        w=""
        c=0
        for j in range(len(num2)-1,-1,-1):

            for i in range(len(num1)-1,-1,-1):
                ans=t[num1[i]]*t[num2[j]]
  
                ans+=carry
                carry=0
                if len(str(ans))==2:
                    carry=int(str(ans)[0])
                    w+=str(ans)[1]
                    
                else:
                    w+=str(ans)
            if carry!=0:
                w+=str(carry)
            w=w[::-1]+str("0")*c
            s.append(int(w))
            
            w=""
            carry=0
            c+=1
 

        return str(sum(s))

                