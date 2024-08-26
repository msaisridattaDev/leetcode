import random
class Solution:

    def __init__(self, nums: List[int]):
        self.l=nums
        self.c={}
        self.t={}
        for i,v in enumerate(self.l):
            if v in self.c.keys():
                self.c[v]+=[i]
            else:
                self.c[v]=[i]

    def pick(self, target: int) -> int:

        if target in self.c and target not in self.t:
            p=self.c[target]
            random.shuffle(p)
            self.c[target]=p
            self.t[target]=0
            return p[0]
        elif target in self.c and target  in self.t:
            p=self.c[target]
            j=self.t[target]
            self.t[target]= (self.t[target]+1)% len(self.c[target])
            return p[j]
        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)