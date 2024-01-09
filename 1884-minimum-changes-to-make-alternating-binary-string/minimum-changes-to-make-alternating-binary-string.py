import copy

class Solution:
    def minOperations(self, s: str) -> int:
        
        l=list(s)
        t=copy.deepcopy(l)
        m,n=0,0
        h=0
        while (h<=len(l)-2):

            if l[h]=="1" and l[h+1]=="1":

                l[h+1]="0"
                m+=1
            elif l[h]=="0" and l[h+1]=="0":
                l[h+1]="1"
                m+=1

            h+=1


        
        
        

        if l[0]=='0':
            t[0]="1"
            n+=1
        else:
            t[0]="0"
            n+=1

        #print(t,l)
        j=0
        while (j<=len(t)-2):

            if t[j]=="1" and t[j+1]=="1":

                t[j+1]="0"
                n+=1
            elif t[j]=="0" and t[j+1]=="0":
                t[j+1]="1"
                n+=1

            j+=1

       # print(m,n)
        return min(m,n)

