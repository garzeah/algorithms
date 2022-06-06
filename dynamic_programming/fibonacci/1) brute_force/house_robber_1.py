class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(nums, 0)

    def helper(self, nums, start):
        # Have no more houses to rob from
        if start >= len(nums):
            return 0

        # Steal from current house and skip one to steal next
        steal_current = nums[start] + self.helper(nums, start + 2)

        # Skip current house to steal from the adjacent house
        skip_current = self.helper(nums, start + 1)

        return max(steal_current, skip_current)

# Time Complexity: O(2^n)
# Space Compelxity: O(2^n) which is used to store the recursion stack
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk