class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        
        self.x=v1
        self.y=v2
        self.flag=True

    def next(self) -> int:


        if self.flag and self.x :
            self.flag=False
            return self.x.pop(0)

        elif not self.flag and self.y :
            self.flag=True
            return self.y.pop(0)
        elif self.flag and not self.x :

            return self.y.pop(0)
        elif not self.flag and not self.y :
            return self.x.pop(0)

        

    def hasNext(self) -> bool:
        if self.x or self.y:
            return True
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())