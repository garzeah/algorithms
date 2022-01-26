class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # We want to find the interval with the earliest end time (greedy approach)
        intervals.sort(key = lambda x : x[1])

        count = 0 # Min. number of intervals we need to remove to make it non-overlapping
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            # Basically we want to find the first overlapping then we'll remove it
            if end > interval[0]: # Overlapping condition
                # Interval with longer end time is removed, we want the interval with
                # the min. end time bc it produces the maximal capacity to hold the
                # rest of the intervals that are non-overlapping
                end = min(end, interval[1])
                count += 1
            else: # Trying the next interval
                end = interval[1]

        return count

# Time Complexity: O(nlogn)
# Space Complexity: O(1)