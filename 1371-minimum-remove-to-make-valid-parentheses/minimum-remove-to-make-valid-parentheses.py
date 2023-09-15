class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        o=[]
        un=[]
        for i in range(len(s)):
            
            if not s[i].isalpha():
                if s[i]=="(":
                    o+=[i]
                else:
            
                    if len(o)!=0:
                        q=o.pop()
                        if q < i:
                            pass
                    else:
                        un+=[i]
        
        if len(o)!=0:
            un.extend(o)

        a=""
        p=0
        if len(un)!=0:
            for j in range(len(s)):
                if j!=un[p]:
                    a+=s[j]
                else:
                    if p<len(un)-1:
                        p+=1
            return a
        else:
            return s