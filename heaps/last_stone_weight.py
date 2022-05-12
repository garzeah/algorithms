class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heappush(max_heap, -stone)

        while len(max_heap) > 1:
            temp = -heappop(max_heap) - -heappop(max_heap)
            heappush(max_heap, -temp)

        return -max_heap[0]

# Time Complexity: O(n log n)
# Space Complexity: O(n)