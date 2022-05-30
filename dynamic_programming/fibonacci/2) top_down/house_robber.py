class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.find_max_steal_recursive(nums, 0)


    def find_max_steal_recursive(self, nums, start):
        # Have no more houses to rob from
        if start >= len(nums):
            return 0

        # Steal from current house and skip one to steal next
        steal_current = nums[start] + self.find_max_steal_recursive(nums, start + 2)

        # Skip current house to steal from the adjacent house
        skip_current = self.find_max_steal_recursive(nums, start + 1)

        return max(steal_current, skip_current)

# Time Complexity: