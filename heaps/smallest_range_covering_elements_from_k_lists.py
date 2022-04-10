class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        curr_max_num = float('-inf')
        range_start, range_end = 0, float('inf')

        # Put the 1st element of each array in the max heap
        for arr in nums:
            heappush(min_heap, [arr[0], 0, arr])
            curr_max_num = max(curr_max_num, arr[0])

        # Take the smallest (top) element from the min heap,
        # if it gives us smaller range, update the ranges if
        # the array of the top element has more elements,
        # insert the next element in the heap
        while len(min_heap) == len(nums):
            num, i, arr = heappop(min_heap)

            # Keep track of the start and end ranges
            if range_end - range_start > curr_max_num - num:
                range_start = num
                range_end = curr_max_num

            # Want to find the current maximum number
            if len(arr) > i + 1:
                # Insert the next element in the heap
                heappush(min_heap, [arr[i + 1], i + 1, arr])
                curr_max_num = max(curr_max_num, arr[i + 1])

        return [range_start, range_end]

# Time Complexity: Since, at most, we’ll be going through all the elements of
# all the arrays and will remove/add one element in the heap in each step,
# the time complexity of the above algorithm will be O(N*logM) where ‘N’
# is the total number of elements in all the ‘M’ input arrays.

# Space Complexity: The space complexity will be O(M) because, at any time,
# our min-heap will be store one number from all the ‘M’ input arrays.