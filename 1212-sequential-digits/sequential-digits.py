class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        u=['12', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789']
        m=[]
        p=0
        s=u[p]
        m+=[int(s)]
        while(1):
            a=""
            for i in s:
                a+=str(int(i)+1)

            #print(a,s)
            if '10' in a:
                if p< len(u)-1: 
                    p+=1
                    s=u[p]
                    m+=[int(s)]
                else:
                    break
            else:
                m+=[int(a)]
                s=a

            y=[]
            #print(m)
        for j in m:

            if high>= j and low <=j:
                    y+=[j]
    
        return y
        