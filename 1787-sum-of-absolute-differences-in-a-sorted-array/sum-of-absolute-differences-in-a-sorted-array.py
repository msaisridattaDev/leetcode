class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        p=[]
        n=0
        t=[]
        for i in nums:
            n+=i
            p.append(n)

        #print(p)

        b=1
        v=len(nums)-1

        s=0
        s+=abs((v)*nums[0]-(p[v]-p[0]))
        t.append(s)

        while(b<=len(nums)-1):
            s=0
            s+= abs(b*nums[b]-p[b-1])
            s+=abs((v-b)*nums[b]-(p[v]-p[b]))
            t.append(s)

            b+=1

        return t





        