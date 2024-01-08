class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        num1=num1[::-1]
        num2=num2[::-1]

        p1=0
        p2=0
        ans=""
        c=0
        while(p1<=len(num1)-1 and p2<=len(num2)-1 ):

            p=str(int(num1[p1])+int(num2[p2])+int(c))

            if len(p)==2:
                
                
                c=p[0]
                ans+=p[1]
            
            else:
                ans+=p[0]
                c=0

            p1+=1
            p2+=1




        if p2==len(num2) and p1<len(num1) :

            while(p1<=len(num1)-1):

                p=str(int(num1[p1])+int(c))

                if len(p)==2:
                    c=p[0]
                    ans+=p[1]
                else:
                    ans+=p[0]
                    c=0

                p1+=1

        elif p1==len(num1) and p2<len(num2):

            while(p2<=len(num2)-1):

                p=str(int(num2[p2])+int(c))

                if len(p)==2:
                    c=p[0]
                    ans+=p[1]
            
                else:
                    ans+=p[0]
                    c=0

                p2+=1
        
        
        if int(c)>0:
            ans+=str(c)

        ans=ans[::-1]

        return ans


