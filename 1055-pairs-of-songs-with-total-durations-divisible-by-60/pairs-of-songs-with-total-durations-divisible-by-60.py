class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        c={}
        s=0
        l=[]
        for i in time:

            t=i%60
            l+=[t]
            if t in c.keys():
                c[t]+=1
            else:
                c[t]=1

        
            
        r=list(set(l))
        print(sorted(c.items()),s)
        
        for i in r:

            p=i%60   
            
            if p==30 or p==0:
                if p in c.keys():
                    v=c[p]-1
                    s+=int((v*(v+1))/2)
                    


            elif 60-p in c.keys():
                s+=c[60-p]*c[p]
                r.remove(60-p)


            print(i,s)


            
        
        return s

