class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
      i, start, end = 0, 0, 1
      merged = []

      # Find all intervals that come before the 'new_interval'
      while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

      # Merge all intervals that overlap with 'new_interval'
      while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

      # Insert the new_interval
      merged.append(new_interval)

      # Add all the remaining intervals to the output
      while i < len(intervals):
        merged.append(intervals[i])
        i += 1

      return merged

# Time Complexity: O(n)
# Space Complexity: O(n)