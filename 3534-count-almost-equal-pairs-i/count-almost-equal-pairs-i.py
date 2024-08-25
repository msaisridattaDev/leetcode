class Solution:
    def countPairs(self, nums: List[int]) -> int:

        cnt=0

        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):


                p=str(nums[i])

                q=str(nums[j])

                if Counter(p)==Counter(q):

                    #print("Map is same",p,q)
                    pass

                if len(p)< len(q):
                    p="0"*(len(q)-len(p))+p
                else:
                    q="0"*(len(p)-len(q))+q

                p1=0
                p2=0
                t=0
                w=""

                if p==q:
                    cnt+=1

                else:

                    while(p1< len(p) and p2 < len(q)):

                        if p[p1]!=q[p2]:
                            t+=1
                        
                        p1+=1
                        p2+=1
                        

                if t==2 and Counter(p)==Counter(q):
                    cnt+=1

        return cnt

        