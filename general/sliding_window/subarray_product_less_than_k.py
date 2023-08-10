class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Negative numbers, 0 and 1 would break this
        if k <= 1:
            return 0

        start, count, window_product = 0, 0, 1

        for end in range(len(nums)):
            window_product *= nums[end]

            # Shrink the window since it is >= k
            while window_product >= k:
                window_product /= nums[start]
                start += 1

            # Adding the size of the window to our count
            # returns the number of contiguous subarrays
            # where the product of all the elements in
            # the subarray is < k
            count += end - start + 1

        return count

# Time Complexity: The outer for loop runs for all elements, and
# the inner while loop processes each element K times (the amount of
# times we divide before being less than target) once; therefore,
# the time complexity of the algorithm will be O(N+KN), which is
# asymptotically equivalent to O(N).

# Space Complexity: O(1)