class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        return self.helper(nums, memo, 0)

    def helper(self, nums, memo, index):
        # If we have reached the last index
        if (index >= len(nums) - 1):
            return 0

        if index in memo:
            return memo[index]

        # Initializing jumps with maximum value. It will store
        # the minimum jumps required to reach the current index
        jumps = float('inf')

        # Checking all the possible jumps. Want to check after
        # the current index and the indexes it has access too
        for i in range(index + 1, index + nums[index] + 1):
            # Selecting the minimum jump
            jumps = min(jumps, self.helper(nums, memo, i) + 1)

        memo[index] = jumps
        return memo[index]

# TC: O(n^2)
# SC: O(n)