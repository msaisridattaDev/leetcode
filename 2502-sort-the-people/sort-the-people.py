class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        c={}
        t=[]
        for i,v in enumerate(names):

            if heights[i] not in c.keys():
                c[heights[i]]=v

        heights.sort()
        heights.reverse()
        print(c,heights)
        for j in heights:
            t.append(c[j])

        return t

