class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            # We have two choices for each index we need to consider
            # which is, is it better to start a new subarray or is
            # it better to keep building the contiguous subarray
            curr_sum = max(nums[i], nums[i] + curr_sum)
            max_sum = max(max_sum, curr_sum)

        return max_sum

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=2MmGzdiKR9Y
