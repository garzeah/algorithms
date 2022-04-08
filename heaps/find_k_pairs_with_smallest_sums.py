class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap, output = [], []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                curr_num = -(nums1[i] + nums2[j])

                if len(max_heap) < k:
                    heappush(max_heap, (curr_num, i, j))
                else:
                    # If the sum of the two numbers from the two arrays is smaller
                    # than the smallest (top) element of the heap, we can 'break'
                    # here. Since the arrays are sorted in the descending order,
                    # we'll not be able to find a pair with a higher sum moving forward
                    if curr_num < max_heap[0][0]:
                        break
                    # We have a pair with a larger sum, remove top and insert this pair in the heap
                    else:
                        heappop(max_heap)
                        heappush(max_heap, (curr_num, i, j))

        for (num, i, j) in max_heap:
            output.append([nums1[i], nums2[j]])

        return output

# Time Complexity: Since, at most, we’ll be going through all the elements of both
# arrays and we will add/remove one element in the heap in each step, the time
# complexity of the above algorithm will be O(N*M*logK) where ‘N’ and ‘M’ are
# the total number of elements in both arrays, respectively. If we assume that
# both arrays have at least ‘K’ elements then the time complexity can be
# simplified to O(K^2logK), because we are not iterating more than ‘K’
# elements in both arrays.

# Space Complexity: The space complexity will be O(K) because, at any time,
# our max heap will be storing ‘K’ largest pairs.