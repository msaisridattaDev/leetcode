class Logger:

    def __init__(self):
        
        self.c={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.c.keys():
            v=self.c[message].pop()
            if timestamp-v>=10:
                self.c[message]=[timestamp]
                return True
            else:
                self.c[message]=[v]
                return False

        else:
            self.c[message]=[timestamp]
            return True




# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)