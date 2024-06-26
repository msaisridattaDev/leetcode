class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        t={}
        r={}
        w=""
        k=[]
        maxi=0
        for i,v in enumerate(s):

           # print(w,k)

            if v in t:
                j=t[v]
                t[v]=i
                k.remove(j)
                k.append(i)
                r[i]=v
                w+=v
            else:
                if len(t)==2:
                    b=min(k)
                    #print("b is",b)
                    n=w.rindex(r[b])


                    k.remove(b)
                    
                    w=w[n+1::]

                    t.pop(r[b])
                    r.pop(b)
                    
                t[v]=i
                k.append(i)
                r[i]=v
                w+=v

            if len(w)>maxi:
                maxi=len(w)

        return maxi
                

                




            

        

