class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(nums, 0)

    def helper(self, nums, i):
        # Have no more houses to rob from
        if i >= len(nums):
            return 0

        # In example [1, 2, 3, 1], we have 2 decisions when trying
        # to find the maximum amount of money we can rob tonight
        # 1) The decision to rob the current house and the remaining
        # houses that are not adjacent to it
        # 2) The decision to rob the adjacent house and the remaining
        # houses that are not adjacent to it
        rob_curr = nums[i] + self.helper(nums, i + 2)
        rob_adj = self.helper(nums, i + 1)

        return max(rob_curr, skip_current)

# Time Complexity: O(2^n)
# Space Compelxity: O(2^n) which is used to store the recursion stack
# Solution: https://www.youtube.com/watch?v=73r3KWiEvyk