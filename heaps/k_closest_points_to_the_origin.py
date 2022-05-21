class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap, output = [], []

        for (x, y) in points:
            dist = -(x*x + y*y)

            if len(max_heap) < k:
                heappush(max_heap, (dist, x, y))
            else:
                # Only adding the distance if it is smaller
                if dist < -max_heap[0][0]:
                    heappushpop(max_heap, (dist, x, y))

        for (dist, x, y) in max_heap:
            output.append([x, y])

        return output

# Time Complexity: O(n*logk) where k is the amount of elements inside our heap
# and n is for iterating through the points.

# Space Complexity: O(k)