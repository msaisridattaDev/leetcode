class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        t=[]

        for j in cpdomains:

            p=j.split(".")

            v=p[0].split()+p[1::]

            t.append(v)

       

        c={}

        for u in t:

            for f in range(1,len(u)):

                y=".".join(u[f::])

                if y not in c.keys():
                    c[y]=int(u[0])
                else:
                    c[y]+=int(u[0])
        
        z=[]
        for m,n in c.items():

            d= str(n)+" "+m
            z.append(d)


        return z
