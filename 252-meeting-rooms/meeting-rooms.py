class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()


        for j in range(len(intervals)-1):

            if intervals[j][1] <= intervals[j+1][0]:
                pass
            else:
                return False
        
        return True
