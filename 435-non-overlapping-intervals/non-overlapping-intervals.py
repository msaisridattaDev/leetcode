class Solution:
    def eraseOverlapIntervals(self,intervals):
        if not intervals:
            return 0

        # Step 1: Sort by the end of intervals
        intervals.sort(key=lambda x: x[1])

        # Initialize variables
        end = intervals[0][1]
        count = 0

        # Step 2: Check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1  # This interval needs to be removed
            else:
                end = intervals[i][1]  # Update the end to the current interval's end

        return count
