class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            heappush(self.min_heap, num)

            if len(self.min_heap) > k:
                heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        return self.min_heap[0]

# Time Complexity:
# Initializing the class takes nlogk time where n is the length of
# nums and k is the amount

# The add method takes log(1) time.

# Space Complexity: O(k)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)