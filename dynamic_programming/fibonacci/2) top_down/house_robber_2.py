class Solution:
    def rob(self, nums: List[int]) -> int:
        # When we only have 1 house
        if len(nums) == 1:
            return nums[0]

        # When we have 2 houses, choose max of 2 houses
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]
        return max(
            self.helper(dp1, nums[1:], 0),
            self.helper(dp2, nums[:-1], 0)
        )

    def helper(self, dp, nums, idx):
        if idx >= len(nums):
            return 0

        if dp[idx] == 0:
            # Steal from current house and skip one to steal next
            steal_current = nums[idx] + self.helper(dp, nums, idx + 2)

            # Skip current house to steal from the adjacent house
            skip_current = self.helper(dp, nums, idx + 1)

            dp[idx] = max(steal_current, skip_current)

        return dp[idx]

# Time Complexity: O(2^n)
# Space Compelxity: O(n) which is used to store the memoized calls
# Solution: https://www.youtube.com/watch?v=rWAJCfYYOvM