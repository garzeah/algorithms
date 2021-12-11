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