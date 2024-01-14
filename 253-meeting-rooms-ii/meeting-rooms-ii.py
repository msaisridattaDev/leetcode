import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        t=[intervals[0]]
        m=0

        for v,i in enumerate(intervals):
            heapq.heapify(t)
            if len(t)!=0:
                r=heapq.heappop(t)
                if r[0]>i[0]:
                    t.append([i[1],i[0]])
                    t.append(r)
                else:
                    t.append([i[1],i[0]])

            if len(t)>m:
                m=len(t)

        return m
