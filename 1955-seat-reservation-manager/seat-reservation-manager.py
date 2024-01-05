import heapq

class SeatManager:

    def __init__(self, n: int):
        
        self.l=list(range(1,n+1))
        heapq.heapify(self.l)

    def reserve(self) -> int:
        
        return heapq.heappop(self.l)

    def unreserve(self, seatNumber: int) -> None:
        
        heapq.heappush(self.l,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)