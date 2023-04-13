class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, res = 0, []
        start, end = 0, 1

        # Find all intervals that come before newInterval
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            res.append(intervals[i])
            i += 1

        # Merge all intervals that overlap with newInterval
        while i < len(intervals) and newInterval[end] >= intervals[i][start]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1

        # Append newInterval
        res.append(newInterval)

        # Add the remaining intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)