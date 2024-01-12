class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        c= words

        p=0
        p1=1

        f={}
        s={}

        while(p1<=len(c)-1):

            
            if len(f)==0:
                for u in c[p]:

                    if u in f.keys():
                        f[u]+=1
                    else:
                        f[u]=1

            for v in c[p1]:

                if v in s.keys():
                    s[v]+=1
                else:
                    s[v]=1

            if f==s:
                c.pop(p1)
                s={}
                #print(c)
            else:
                p+=1
                p1+=1
                f=s
                s={}

        return c