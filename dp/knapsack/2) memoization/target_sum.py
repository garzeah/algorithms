class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # Invalid input since total must be >= target
        if total < abs(target):
            return 0

        # The x is going to range from total * 2 bc of the range of pos/neg of the total
        memo = [ [ -1 for x in range(total * 2 + 1) ] for y in range(len(nums)) ]
        return self.helper(nums, target, 0, memo)

    # Want to find every possible expression that can hit out target
    def helper(self, nums, target, i, memo):
        if i >= len(nums):
            if target == 0:
                return 1

            return 0

        if memo[i][target] != -1:
            return memo[i][target]

        memo[i][target] = self.helper(nums, target - nums[i], i + 1, memo) + self.helper(nums, target + nums[i], i + 1, memo)
        return memo[i][target]


# TC: O(n*m) where n is the length of numbers and m is the target
# SC: O(s) where s is the total of calculations we have to make in each (i, total)
# Solution: https://www.youtube.com/watch?v=g0npyaQtAQM