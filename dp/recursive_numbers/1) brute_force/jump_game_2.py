class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.helper(nums, 0)

    def helper(self, nums, index):
        # If we have reached the last index
        if (index >= len(nums) - 1):
            return 0

        # Initializing jumps with maximum value. It will store
        # the minimum jumps required to reach the current index
        jumps = float('inf')

        # Checking all the possible jumps
        for i in range(index + 1, index + nums[index] + 1):
            # Selecting the minimum jump
            jumps = min(jumps, self.helper(nums, i) + 1)

        return jumps

# TC: O(2^n)
# SC: O(n)