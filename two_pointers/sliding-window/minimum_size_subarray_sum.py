# Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target, nums):
        start = 0
        window_sum = 0
        min_length = float('inf')

        for end in range(0, len(nums)):
            window_sum += nums[end]

            # shrink the window as small as possible
            # until the 'window_sum' is smaller than 'target'
            while window_sum >= target:
                min_length = min(min_length, end - start + 1)
                window_sum -= nums[start]
                start += 1

        if (min_length == float('inf')):
            return 0

        return min_length;

# Time Complexity: The outer for loop runs for all elements, and
# the inner while loop processes each element only once; therefore,
# the time complexity of the algorithm will be O(N+N), which is
# asymptotically equivalent to O(N).

# Space Complexity: O(1)