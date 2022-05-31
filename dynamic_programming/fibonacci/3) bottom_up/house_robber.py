class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]  # '+1' to handle the zero house
        dp[0] = 0  # If there are no houses, the thief can't steal anything
        dp[1] = nums[0]  # Only one house, so the thief have to steal from it

        # Please note that dp[] has one extra element to handle zero house
        for i in range(1, n):
            # We will take the max of stealing from current house and
            # skipping one to steal the next or skipping current
            # house and stealing from the adjacent one
            dp[i + 1] = max(nums[i] + dp[i - 1], dp[i])

        return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)