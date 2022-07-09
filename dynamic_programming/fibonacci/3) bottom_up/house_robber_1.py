class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # When we only have 1 house
        if n == 1:
            return nums[0]

        # When we have 2 houses, choose max of 2 houses
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0 for _ in range(n + 1)]  # '+1' to handle the zero house
        rob_curr = nums[0]  # If there are no houses, the thief can't steal anything
        rob_adj = max(nums[0], nums[1])  # Only one house, so the thief have to steal from it

        # Please note that dp[] has one extra element to handle zero house
        for i in range(2, n):
            # We will take the max of stealing from current house and
            # skipping one to steal the next or skipping current
            # house and stealing from the adjacent one
            temp = max(rob_curr + nums[i], rob_adj)
            rob_curr = rob_adj
            rob_adj = temp
            dp[i] = rob_adj

        return dp[n - 1]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk