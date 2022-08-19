class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        min_heap = []

        # Create a min_heap of our [start, end] times and we
        # only want to add the times that can fit our durations
        for (start, end) in slots1:
            if start + duration <= end:
                heappush(min_heap, [start, end])

        for (start, end) in slots2:
            if start + duration <= end:
                heappush(min_heap, [start, end])


        # Compare the previous minimum with the current minimum in the heap
        while len(min_heap) >= 2:
            start, end = heappop(min_heap)

            # If the previous minimum's end time overlaps with the next
            # minimum's start time + the duration then we have the
            # earliest time slot that works for both of the people
            if end >= min_heap[0][0] + duration:
                # Better to take the time ahead since it's overlapping
                return [min_heap[0][0], min_heap[0][0] + duration]

        return []

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/meeting-scheduler/discuss/1181839/Python-heap-solution