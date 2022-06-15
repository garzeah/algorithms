class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # Python sorts by index order
        prev_end = intervals[0][1] # Keep track of first end value
        output = 0

        for start, end in intervals[1:]:
            if start >= prev_end: # Not overlapping
                prev_end = end
            else: # Overlapping
                output += 1
                # We want to keep the value that ends first since
                # if we keep the value that ends last, it will
                # increase the likelihood of an overlap
                prev_end = min(prev_end, end)

        return output

# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=nONCGxWoUfM