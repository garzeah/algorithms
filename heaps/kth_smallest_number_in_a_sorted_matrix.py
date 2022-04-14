class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []

        # Put the 1st element of each row in the min heap we
        # don't need to push more than 'k' elements in the heap
        for row in matrix:
            heappush(min_heap, (row[0], 0, row))

        # Take the smallest (top) element form the min heap, if
        # the running count is equal to k' return the number if
        # the row of the top element has more elements, add the
        # next element to the heap
        k_count = 0
        while min_heap:
            curr_num, i, row = heappop(min_heap)
            num_count += 1

            # We are at the kth element
            if k_count == k:
                return curr_num

            # While can we still index a row
            if len(row) > i + 1:
                heappush(min_heap, [row[i + 1], i + 1, row])

        return None

# Time Complexity: First, we inserted at most ‘K’ or one element
# from each of the ‘N’ rows, which will take O(N). Then we went
# through at most ‘K’ elements in the matrix and remove/add one
# element in the heap in each step. As we can’t have more than
# ‘N’ elements in the heap in any condition, therefore, the
# overall time complexity of the above algorithm will be
# O(N + K*logN).

# Space Complexity: The space complexity will be O(N) because, in the
# worst case, our min-heap will be storing one number from each of the ‘N’ rows.
