class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # Invalid input since total must be >= target
        if total < abs(target):
            return 0

        return self.helper(nums, target, 0)

    # Want to find every possible expression that can hit out target
    def helper(self, nums, target, i):
        if i >= len(nums):
            if target == 0:
                return 1

            return 0

        return self.helper(nums, target - nums[i], i + 1) + self.helper(nums, target + nums[i], i + 1)


# TC: O(2^n) where n is the length of numbers and m is the target
# SC: O(2^n) since we're backtracking and not working in a DFS fashion
# Solution: https://www.youtube.com/watch?v=g0npyaQtAQM