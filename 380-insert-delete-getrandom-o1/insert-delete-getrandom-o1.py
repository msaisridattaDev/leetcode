import random

class RandomizedSet:

    def __init__(self):
        self.c={}

    def insert(self, val: int) -> bool:

        if val in self.c.keys():
            return False
        else:
            self.c[val]=1
            return True
    
    def remove(self, val: int) -> bool:
        if val in self.c.keys():
            self.c.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:

        p=list(self.c.keys())

        return random.choice(p)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()