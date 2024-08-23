class Solution:
    def merge(self,intervals):
        if not intervals:
            return []
        
        # Step 1: Sort intervals based on the start time
        intervals.sort()
        
        merged = [intervals[0]]  # Start with the first interval
        
        # Step 3: Iterate through the sorted intervals
        for current in intervals[1:]:
            last_merged = merged[-1]
            
            if current[0] <= last_merged[1]:  # There is an overlap
                # Merge the current interval with the last one in the merged list
                merged[-1][1] =max(last_merged[1],current[1])
            else:
                # No overlap, add the current interval to the merged list
                merged.append(current)
        
        return merged
