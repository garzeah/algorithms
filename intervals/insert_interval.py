class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        i = 0
        merged = []

        # Find all intervals that come before new_interval
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge all intervals that overlap with 'new_interval'
        while i < len(intervals) and new_interval[1] >= intervals[i][0]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1

        # Append new_interval
        merged.append(new_interval)

        # Add the remaining intervals
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged

# Time Complexity: O(n)
# Space Complexity: O(1)