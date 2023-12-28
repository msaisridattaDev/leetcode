class Solution:
    def reverseVowels(self, s: str) -> str:
        
        p1=0
        p2=len(s)-1
        r=list(s)
        p=""
        t=['a','e','i','o','u','A','E','I','O','U']
        while(p1!=p2 and p1<p2):
            if r[p1] in t and r[p2] in t:
                temp=r[p2]
                r[p2]=r[p1]
                r[p1]=temp
                p1+=1
                p2-=1

            elif r[p1] not in t:

                p1+=1
            
            elif r[p2] not in t:
                p2-=1

        
        return "".join(r)
                 