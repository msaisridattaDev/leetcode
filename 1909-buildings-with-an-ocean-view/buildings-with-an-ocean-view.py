class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        nums=heights
        d=len(nums)-1
        print(nums)
        t=[d]
        l=[nums[-1]]


        for i in range((len(nums))-1,-1,-1):

            p=l.pop()
            #print(p,nums[i])
            if nums[i] >p:
                l.append(p)
                l.append(nums[i])
                t.append(i)
                
            else:
                l.append(p)

        t.sort()
        return t
