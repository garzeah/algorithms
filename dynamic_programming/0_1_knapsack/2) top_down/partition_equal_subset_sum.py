class Solution:
    def canPartition(self, nums):
        target = sum(nums)

        # if 'target' is a an odd number, we can't have two subsets with equal sum
        if target % 2 == 1:
            return False

        # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
        target //= 2
        dp = [[-1 for x in range(target + 1)] for y in range(len(nums))]
        return True if self.helper(dp, nums, target, 0) == 1 else False

    def helper(self, dp, nums, target, idx):
        # base check
        if target == 0:
            return 1

        n = len(nums)
        if n == 0 or idx >= n:
            return 0

        # if we have not already processed a similar problem
        if dp[idx][target] == -1:
            # recursive call after choosing the number at the idx
            # if the number at idx exceeds the target, we shouldn't process this
            if nums[idx] <= target:
                if self.helper(dp, nums, target - nums[idx], idx + 1) == 1:
                    dp[idx][target] = 1
                    return 1

            # recursive call after excluding the number at the idx
            dp[idx][target] = self.helper(dp, nums, target, idx + 1)

        return dp[idx][target]