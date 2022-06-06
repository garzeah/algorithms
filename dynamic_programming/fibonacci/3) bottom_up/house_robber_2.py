class Solution:
    def rob(self, nums: List[int]) -> int:
        # When we only have 1 house
        if len(nums) == 1:
            return nums[0]

        # When we have 2 houses, choose max of 2 houses
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )

    def helper(self, nums):
        n = len(nums)

        # When we only have 1 house
        if len(nums) == 1:
            return nums[0]

        # When we have 2 houses, choose max of 2 houses
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0 for _ in range(n)]
        steal_current = nums[0]  # If there are no houses, the thief can't steal anything
        skip_current = max(nums[0], nums[1])  # Only one house, so the thief have to steal from it

        # Please note that dp[] has one extra element to handle zero house
        for i in range(2, n):
            # We will take the max of stealing from current house and
            # skipping one to steal the next or skipping current
            # house and stealing from the adjacent one
            temp = max(steal_current + nums[i], skip_current)
            steal_current = skip_current
            skip_current = temp
            dp[i] = skip_current

        return dp[n - 1]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=rWAJCfYYOvM