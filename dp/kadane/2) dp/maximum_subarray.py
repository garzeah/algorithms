class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            # If our curr_sum to the left of our current number is negative,
            # we want to reset the curr_sum to 0 because we're being greedy
            # and want to find the maximum subarray
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=5WZl3MMT0Eg
