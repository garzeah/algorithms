class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (i, curr_sum)
        return self.backtrack(nums, target, memo, 0, 0)

    # We are using backtracking bc we are finding all
    # the different ways we can get to our target
    def backtrack(self, nums, target, memo, total, i):
        # We are at the end, return 1 or 1 depending on if total matches target
        if i == len(nums):
            return 1 if total == target else 0

        # We have already calculated this, fetch from cache
        if (i, total) in memo:
            return memo[(i, total)]

        memo[(i, total)] = (
            self.backtrack(nums, target, memo, total + nums[i], i + 1) +
            self.backtrack(nums, target, memo, total - nums[i], i + 1)
        )
        return memo[(i, total)]


# TC: O(n*m) where n is the length of numbers and m is the target
# SC: O(s) where s is the total of calculations we have to make in each (i, total)
# Solution: https://www.youtube.com/watch?v=g0npyaQtAQM