class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        flag=False
        if x in arr:
            u=arr.index(x)
            
        else:
            f=bisect_left(arr,x)
            arr=arr[0:f]+[x]+arr[f::]
            flag=True
            u=arr.index(x)
            


        if u>=0:
            if not flag:
                p1=u
            else:
                p1=u-1
        
        if u<=len(arr)-1:
            p2=u+1

        t=[]
        while(p1>=0 and p2<=len(arr)-1 and k>0):

            if abs(arr[p1]-x) < abs(arr[p2]-x):

                t.append(arr[p1])
                p1-=1

            elif abs(arr[p1]-x)== abs(arr[p2]-x):

                t.append(arr[p1])
                p1-=1

            else:
                t.append(arr[p2])
                p2+=1
        
            k-=1

        while(p1<0 and p2<=len(arr)-1 and k>0):

            t.append(arr[p2])
            p2+=1
            k-=1

        while(p1>=0 and p2>len(arr)-1 and k>0):

            t.append(arr[p1])
            p1-=1
            k-=1

        t.sort()
        return t



        
