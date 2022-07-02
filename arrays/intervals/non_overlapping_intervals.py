class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        prev_end = intervals[0][1]
        res = 0

        # As we iterate through each interval, we want to
        # check for an overlap and when we have one, we
        # want to keep the smallest end in order to
        # not make it overlap
        for curr_start, curr_end in intervals[1:]:
            if prev_end > curr_start: # Overlapping
                res += 1
                prev_end = min(prev_end, curr_end)
            else: # Not overlapping
                prev_end= curr_end

        return res

# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=nONCGxWoUfM