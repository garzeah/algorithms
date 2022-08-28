class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(nums, 0)

    def helper(self, nums, i):
        # Have no more houses to rob from
        if i >= len(nums):
            return 0

        # Steal from current house and skip one to steal next
        rob_curr = nums[i] + self.helper(nums, i + 2)

        # Skip current house to steal from the adjacent house
        rob_adj = self.helper(nums, i + 1)

        return max(rob_curr, skip_current)

# Time Complexity: O(2^n)
# Space Compelxity: O(2^n) which is used to store the recursion stack
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk