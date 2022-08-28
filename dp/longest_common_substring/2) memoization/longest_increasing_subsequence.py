class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for x in range(len(nums) + 1)] for y in range(len(nums))]
        return self.helper(nums, dp, -1, 0)

    def helper(self, nums, dp, prev, i):
        if i == len(nums):
            return 0

        # Want to check if the next number is greater than the
        # previous number when building our subsequence
        if dp[i][prev + 1] == -1:
            count1 = 0
            if prev == -1 or nums[i] > nums[prev]:
                count1 = 1 + self.helper(nums, dp, i, i + 1)

            count2 = self.helper(nums, dp, prev, i + 1)
            dp[i][prev + 1] = max(count1, count2)

        return dp[i][prev + 1]


# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Solution: Grokking