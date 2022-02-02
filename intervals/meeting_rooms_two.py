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

        for i in range(len(intervals)):
            # Checking for free rooms
            if ends[end] > starts[i]:
                rooms += 1
            # Not a free room and check the next end pointer
            else:
                end += 1

        return rooms

# Time Complexity: O(nlogn)
# Space Complexity: O(n)