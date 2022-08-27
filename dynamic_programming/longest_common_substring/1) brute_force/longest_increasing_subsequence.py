class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for x in range(len(nums) + 1)] for y in range(len(nums))]
        return self.helper(nums, float('-inf'), 0)

    def helper(self, nums, prev, i):
        if i == len(nums):
            return 0

        # Want to check if the next number is greater than the
        # previous number when building our subsequence
        count1 = 0
        if nums[i] > prev:
            count1 = 1 + self.helper(nums, nums[i], i + 1)

        count2 = self.helper(nums, prev, i + 1)

        return max(count1, count2)


# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Solution: Grokking