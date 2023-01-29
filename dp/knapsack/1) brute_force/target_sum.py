class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.backtrack(nums, target, 0, 0)

    # We are using backtracking bc we are finding all
    # the different ways we can get to our target
    def backtrack(self, nums, target, total, i):
        # We are at the end, return 1 or 1 depending on if total matches target
        if i == len(nums):
            return 1 if total == target else 0

        return (
            self.backtrack(nums, target, total + nums[i], i + 1) +
            self.backtrack(nums, target, total - nums[i], i + 1)
        )


# TC: O(2^n) where n is the length of numbers and m is the target
# SC: O(2^n) since we're backtracking and not working in a DFS fashion
# Solution: https://www.youtube.com/watch?v=g0npyaQtAQM