class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [ [ -1 for x in range(target + 1) ] for y in range(len(nums)) ]
        return self.helper(nums, target, memo, 0)

    def helper(self, nums, target, memo, i):
        if target == 0:
            return 1

        if target < 0 or i >= len(nums):
            return 0

        if memo[i][target] != -1:
            return memo[i][target]

        count1 = 0
        if nums[i] <= target:
            count1 += self.helper(nums, target - nums[i], memo, 0)

        count2 = self.helper(nums, target, memo, i + 1)

        memo[i][target] = count1 + count2
        return memo[i][target]