class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []

        for num in arr:
            curr_dist = abs(num - x)

            if len(max_heap) < k:
                heappush(max_heap, [-curr_dist, num])
            else:
                # If we have a smaller distance, then store it. We didn't add
                # and else: break because a larger value could be closer
                # so we want to search the rest of the numbers
                if curr_dist < -max_heap[0][0]:
                    heappushpop(max_heap, [-curr_dist, num])

        output = []
        for (curr_dist, num) in max_heap:
            output.append(num)

        return sorted(output)

# Time Complexity: O(n*logk) where k is the amount of elements inside our heap
# and n is for iterating through the numbers.

# Space Complexity: O(k)