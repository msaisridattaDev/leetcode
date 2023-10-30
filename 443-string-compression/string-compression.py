class Solution:
    def compress(self, chars: List[str]) -> int:

        p1=0
        p2=1
        flag=False
        
        if len(chars)>=1:
            c=1
        while(p1<=len(chars)-1 and p2<=len(chars)-1):

            if chars[p1]==chars[p2]:
                c+=1
    
                if p2-p1>5:
                    chars.pop(p2)
                else:
                    p2+=1
            else:
               
                p=str(c)
                q=0
                if c!=1:
                    #print(chars,p1+1,p2)
                    for i in range(p1+1,p2):
                        if len(p)-1>=q:
                            
                            chars[i]=p[q]
                            q+=1
                        else:
                            if not flag:
                                j=i
                                flag=True
                            chars.pop(j)
                    flag=False
                            
                
                if c==1:
                    p1+=1
                else:
                    #if p1!=0:
                       # print(p1,p,chars)
                    p1=p1+len(p)+1
                    #else:
                       # p1=p1+len(p)+1
                      
                p2=p1+1
                c=1
        p=str(c)
        q=0
        if c!=1:
                    #print(chars,p1+1,p2)
            for i in range(p1+1,p2):
                if len(p)-1>=q:
                                
                    chars[i]=p[q]
                    q+=1
                else:
                    if not flag:
                        j=i
                        flag=True
                    chars.pop(j)
            flag=False
        
        
        





                

        