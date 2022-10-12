class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []

        for i in range(len(intervals)):
            starts.append(intervals[i][0])
            ends.append(intervals[i][1])

        starts.sort()
        ends.sort()

        # Min. number of rooms and 'end' points
        # to the first available room
        rooms, end = 0, 0

        # For each time a meeting begins, we want
        # to check how many times a meeting will start
        for start in starts:
            # Meetings that have started but nothing has
            # ended so we will need a room to accomodate
            if start < ends[end]: # Overlapping
                rooms += 1
            # Check the other ending times
            else:
                end += 1

        return rooms

# Time Complexity: O(nlogn)
# Space Complexity: O(n)