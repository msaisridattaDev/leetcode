class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c={}

        for i in arr:
            if i in c.keys():
                c[i]+=1
            else:
                c[i]=1

        if len(c.values())==len(set(c.values())):
            return True

        

        
