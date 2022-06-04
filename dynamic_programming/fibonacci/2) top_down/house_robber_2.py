class Solution:
    def rob(self, nums: List[int]) -> int:
        # When we only have 1 house
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]
        return max(
            self.rob_recursive(dp1, nums[1:], 0),
            self.rob_recursive(dp2, nums[:-1], 0)
        )

    def rob_recursive(self, dp, nums, start):
        if start >= len(nums):
            return 0

        if dp[start] == 0:
            # Steal from current house and skip one to steal next
            steal_current = nums[start] + self.rob_recursive(dp, nums, start + 2)

            # Skip current house to steal from the adjacent house
            skip_current = self.rob_recursive(dp, nums, start + 1)

            dp[start] = max(steal_current, skip_current)

        return dp[start]

# Time Complexity: O(2^n)
# Space Compelxity: O(n) which is used to store the memoized calls
# Solution: https://www.youtube.com/watch?v=rWAJCfYYOvM