class Solution:
    def countPrimes(self, n: int) -> int:
        l=[]
        p=int((n+1)/2)
        for j in range(p):
            x=[0,1]
            l.extend(x)

        k=2
        for i in range(2,len(l)):

            temp=i
            if l[i]==1:

                while n>=temp*k:
                    if temp*k<=len(l)-1:
                        l[temp*k]=0
                    k+=1
        
                k=2
                i=temp
        


            
        if n>2:
            if n%2==0:
                return sum(l[2:len(l)])+1
            else:
                return sum(l[2:len(l)-1])+1


        return 0


            