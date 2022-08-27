class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        return self.helper(dp, nums, 0)

    def helper(self, dp, nums, i):
        if i >= len(nums):
            return 0

        if dp[i] == 0:
            # Steal from current house and skip one to steal next
            rob_curr = nums[i] + self.helper(dp, nums, i + 2)

            # Skip current house to steal from the adjacent house
            rob_adj = self.helper(dp, nums, i + 1)

            dp[i] = max(rob_curr, rob_adj)

        return dp[i]

# Time Complexity: O(2^n)
# Space Compelxity: O(n) which is used to store the memoized calls
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk