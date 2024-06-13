class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d=[None]*len(nums)
        d[0]=nums[0]
    
        l=[]
        l.append(d[0]%k)
        t={}
        t[d[0]%k]=[0]
        for i in range(1,len(nums)):

            d[i]=d[i-1]+nums[i]

            if d[i]%k==0:
                return True

            if d[i]==d[i-1]:
                l.append(0)
                p=0
                if p in t.keys():
                    t[p]+=[i]
                else:
                    t[p]=[i]
                continue

            p=d[i]%k
            l.append(d[i]%k)
            if p in t.keys():
                t[p]+=[i]
            else:
                t[p]=[i]
                
        print(t,l)

        if 0 in t.keys():
            for h in range(len(t[0])):
                if h+1<= len(t[0])-1 and t[0][h]+1==t[0][h+1] :
                    return True

        for j in l:
            if j in t.keys() and j!=0:
                if t[j][-1]-t[j][0]>1:
                    return True
                    
            


        return False

            

          
           