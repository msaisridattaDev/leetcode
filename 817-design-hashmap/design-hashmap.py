class MyHashMap:

    def __init__(self):
        self.c={}

    def put(self, key: int, value: int) -> None:
        
        if key in self.c.keys():
            self.c[key]=value
        else:
            self.c[key]=value

    def get(self, key: int) -> int:

        if key in self.c.keys():
            return self.c[key]
        else:
            return -1

    def remove(self, key: int) -> None:

        if key in self.c.keys():
            return self.c.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)