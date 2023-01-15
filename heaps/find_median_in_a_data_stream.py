class MedianFinder:
    def __init__(self):
        # Want the smaller values to go in here, will use a max heap
        # so that when we're finding the median it'll be at the root
        self.max_heap = []
        # Want the larger values to go in here, will use a min heap
        # so that when we're finding the median it'll be at the root
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)

        # Make sure every num in small is less than every num in large to
        # maintain our sorted order when if we were to "combine" min and max heaps
        if (self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]):
            # If not then pop from small and add to large
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)

        # If the size difference is 2 or greater for
        # small then pop from small and add to large
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)

        # If the size difference is 2 or greater for
        # large then pop from large and add to small
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = -heappop(self.min_heap)
            heappush(self.max_heap, val)

    def findMedian(self) -> float:
        # Since it is odd, return the median
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        # Otherwise it is even
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# Time Complexity: The time complexity of the insertNum() will be O(logN)
# due to the insertion in the heap. The time complexity of the findMedian()
# will be O(1) as we can find the median from the top elements of the heaps.

# Space Complexity: The space complexity will be O(N) because, as at any
# time, we will be storing all the numbers.

# Solution: https://www.youtube.com/watch?v=Z6idIicFDOE