class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        curr_end = float('-inf') # Holds curr_end of each lists
        start, end = 0, float('inf')

        # Inserting the 1st element of each array in the min heap
        # Want to keep track of the current largest number we
        # have inserted into the min heap as well
        for arr in nums:
            heappush(min_heap, [arr[0], 0, arr])
            curr_end = max(curr_end, arr[0])

        # Take the smallest (top) element from the min heap,
        # if it gives us smaller range, update the ranges if
        # the array of the top element has more elements,
        # insert the next element in the heap
        # If they didn't equal then we can't get range of all
        # 3 since we ran of out values if one of the array
        while len(min_heap) == len(nums):
            curr_start, i, arr = heappop(min_heap)

            # Want to find the smallest range between these pair of numbers
            if end - start > curr_end - curr_start:
                start = curr_start
                end = curr_end

            # If the array still has remaining elements, go to the next value
            if len(arr) > i + 1:
                # Insert the next value and keep track of the current max num
                heappush(min_heap, [arr[i + 1], i + 1, arr])
                curr_end = max(curr_end, arr[i + 1])

        return [start, end]

# Time Complexity: Since, at most, we’ll be going through all the elements of
# all the arrays and will remove/add one element in the heap in each step,
# the time complexity of the above algorithm will be O(N*logk) where ‘N’
# is the total number of elements in all the ‘k’ input arrays.

# Space Complexity: The space complexity will be O(k) because, at any time,
# our min-heap will be store one number from all the ‘k’ input arrays.