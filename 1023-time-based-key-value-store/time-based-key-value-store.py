import heapq
class TimeMap:

    def __init__(self):
        self.c={}
        self.c2={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.c.keys():
            if timestamp not in self.c[key].keys():
                self.c[key][timestamp]=value
                self.c2[key]=timestamp
        else:
            self.c[key]={}
            self.c[key][timestamp]=value
            self.c2[key]=timestamp
           
       # print(self.c[key].keys())

    def get(self, key: str, timestamp: int) -> str:
        if key in self.c.keys():
            
            u=self.c2[key]

            
            if timestamp not in self.c[key].keys() and timestamp > u :

                return  self.c[key][u]

            elif timestamp not in self.c[key].keys():
    
                
                v=list(self.c[key].keys())
                l=0
                h=len(v)-1
                u=v[-1]
                while(l<=h):

                    m=int((l+h)/2)
                    #print(v[m],timestamp)

                    if v[m] < timestamp:
                        u=v[m]
                        l=m+1
                    elif v[m] > timestamp:
                        h=m-1

                if u>timestamp:
                    #print(u,timestamp)
                    return ""
                
                return self.c[key][u]

            else:
                return self.c[key][timestamp]
        else:
            #print(key)
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)