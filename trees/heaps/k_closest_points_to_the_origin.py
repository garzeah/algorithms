class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap, output = [], []

        for (x, y) in points:
            dist = -(x * x + y * y)
            heappush(max_heap, (dist, x, y))

            # Getting the max k distances
            if len(max_heap) > k:
                heappop(max_heap)

        for (dist, x, y) in max_heap:
            output.append([x, y])

        return output

# Time Complexity: O(n*logk)
# Space Complexity: O(k)