class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap, output = [], []

        for num in arr:
            curr_dist = abs(num - x)

            if len(max_heap) < k:
                heappush(max_heap, [-curr_dist, num])
            else:
                # If the smallest distance is bigger than the current
                # distance, record new smallest distance
                if -max_heap[0][0] > curr_dist:
                    heappop(max_heap)
                    heappush(max_heap, [-curr_dist, num])

        for (curr_dist, num) in max_heap:
            output.append(num)

        return sorted(output)

# Time Complexity: O(n*logk) where k is the amount of elements inside our heap
# and n is for iterating through the numbers.

# Space Complexity: O(k)