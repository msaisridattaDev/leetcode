class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        h=""
        for i in digits:
            h+=str(i)

        a=str(int(h)+1)
        v=[]
        for j in a:
            v+=[int(j)]

        return v


        


        