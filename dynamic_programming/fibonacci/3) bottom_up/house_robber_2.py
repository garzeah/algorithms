class Solution:
    def rob(self, nums: List[int]) -> int:
        # When we only have 1 house
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(
            self.rob_recursive(nums[1:]),
            self.rob_recursive(nums[:-1])
        )

    def rob_recursive(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n + 1)]  # '+1' to handle the zero house
        dp[0] = nums[0]  # If there are no houses, the thief can't steal anything
        dp[1] = max(nums[0], nums[1])  # Only one house, so the thief have to steal from it

        # Please note that dp[] has one extra element to handle zero house
        for i in range(2, n):
            # We will take the max of stealing from current house and
            # skipping one to steal the next or skipping current
            # house and stealing from the adjacent one
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=rWAJCfYYOvM