class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap, output = [], []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                curr_sum = nums1[i] + nums2[j]

                if len(max_heap) < k:
                    heappush(max_heap, [-curr_sum, i, j])
                else:
                    # If we find a smaller sum, pop and add it in
                    if curr_sum < -max_heap[0][0]:
                        heappushpop(max_heap, [-curr_sum, i, j])
                    # No point in checking and move to next sum
                    else:
                        break

        for (num, i, j) in max_heap:
            output.append([nums1[i], nums2[j]])

        return output

# Time Complexity: Since, at most, we’ll be going through all the elements of both
# arrays and we will add/remove one element in the heap in each step, the time
# complexity of the above algorithm will be O(N*M*logK) where ‘N’ and ‘M’ are
# the total number of elements in both arrays, respectively.

# Space Complexity: The space complexity will be O(K) because, at any time,
# our max heap will be storing ‘K’ largest pairs. K represents what we put
# into the heap, that being the sum, i, and j indexes.