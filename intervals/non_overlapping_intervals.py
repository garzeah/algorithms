class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # We want to find the interval with the earliest end time (greedy approach)
        intervals.sort(key = lambda x: x[1])
        count = 0 # Min. number of intervals we need to remove to make it non-overlapping
        prev_end = float('-inf')

        for curr_start, curr_end in intervals:
            if prev_end > curr_start: # Overlapping condition
                # Interval with longer interval is removed, we want the interval with
                # the min. end time bc it produces the maximal capacity to hold the
                # rest of the intervals that are non-overlapping
                prev_end = min(prev_end, curr_end)
                count +=1
            else: # Trying the next interval
                prev_end = curr_end

        return count

# Time Complexity: O(nlogn)
# Space Complexity: O(1)