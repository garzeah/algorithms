class Solution:
    def rob(self, nums: List[int]) -> int:
        # When we only have 1 house
        if len(nums) == 1:
            return nums[0]

        # When we have 2 houses, choose max of 2 houses
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(
            self.helper(nums[1:], 0),
            self.helper(nums[:-1], 0)
        )

    def helper(self, nums, idx):
        # Have no more houses to rob from
        if idx >= len(nums):
            return 0

        # Steal from current house and skip one to steal next
        rob_curr = nums[idx] + self.helper(nums, idx + 2)

        # Skip current house to steal from the adjacent house
        rob_adj = self.helper(nums, idx + 1)

        return max(rob_curr, rob_adj)

# Time Complexity: O(2^n^2)
# Space Compelxity: O(2^n^2) which is used to store the recursion stack
# Solution: https://www.youtube.com/watch?v=rWAJCfYYOvM