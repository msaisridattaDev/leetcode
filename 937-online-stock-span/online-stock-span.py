class StockSpanner:

    def __init__(self):
        self.stack = []


    def next(self, price: int) -> int:

        stack, span = self.stack, 1
        
        while stack and stack[-1][0] <= price:
            span += stack[-1][1]
            stack.pop()
        stack.append((price, span))
        
        return span