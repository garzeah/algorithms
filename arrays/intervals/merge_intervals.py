class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting by start time
        intervals.sort(key = lambda x: x[0])

        merged_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            # Overlapping intervals, determine the higher end time
            if interval[0] <= end:
                end = max(end, interval[1])
            # Non-overlapping intervals, we push a new interval in
            else:
                merged_intervals.append([start, end])
                start = interval[0]
                end = interval[1]

        # Adding the last interval
        merged_intervals.append([start, end])
        return merged_intervals

# Time Complexity: O(nlogn) bc of sorting
# Space Complexity: O(n)