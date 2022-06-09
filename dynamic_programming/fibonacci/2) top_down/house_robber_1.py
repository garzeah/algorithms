class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        return self.helper(dp, nums, 0)

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
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk