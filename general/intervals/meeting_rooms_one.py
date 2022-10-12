class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sorting by start time
        intervals.sort(key=lambda x : x[0])

        for i in range(1, len(intervals)):
            # Checking for an overlap, if one exists
            # can't attend all meetings
            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True

# Time Complexity: O(nlogn) because of sorting
# Space Complexity: O(1)