class MedianFinder:
    def __init__(self):
        # Want the smaller values to go in here, will use a max heap
        # so that when we're finding the median it'll be at the root
        self.small = []
        # Want the larger values to go in here, will use a min heap
        # so that when we're finding the median it'll be at the root
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        # Make sure every num in small is less than every
        # num in large to maintain our sorted order
        if (self.small and self.large and -self.small[0] > self.large[0]):
            # If not then pop from small and add to large
            val = -heappop(self.small)
            heappush(self.large, val)

        # If the size difference is 2 or greater for
        # small then pop from small and add to large
        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)

        # If the size difference is 2 or greater for
        # large then pop from large and add to small
        if len(self.large) > len(self.small) + 1:
            val = -heappop(self.large)
            heappush(self.small, val)

    def findMedian(self) -> float:
        # Since it is odd, return the median
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        # Otherwise it is even
        return (-self.small[0] + self.large[0]) / 2

# Time Complexity: The time complexity of the insertNum() will be O(logN)
# due to the insertion in the heap. The time complexity of the findMedian()
# will be O(1) as we can find the median from the top elements of the heaps.

# Space Complexity: The space complexity will be O(N) because, as at any
# time, we will be storing all the numbers.

# Solution: https://www.youtube.com/watch?v=Z6idIicFDOE