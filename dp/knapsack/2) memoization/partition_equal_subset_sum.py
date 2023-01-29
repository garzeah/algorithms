class Solution:
    def canPartition(self, nums):
        target = sum(nums)

        # if 'target' is a an odd number, we can't have two subsets with equal sum
        if target % 2 == 1:
            return False

        target //= 2 # getting equal subset sum
        # initialize the 'dp' array, -1 for default
        dp = [[-1 for x in range(target + 1)] for y in range(len(nums))]
        return self.helper(nums, dp, target, 0)

    def helper(self, nums, dp, target, i):
        # base check
        if target == 0:
            return True

        if target < 0 or i >= len(nums):
            return False

        # if we have not already processed a similar problem
        if dp[i][target] == -1:
            # recursive call after choosing the number at the i
            # if the number at i exceeds the target, we shouldn't process this
            if nums[i] <= target:
                if self.helper(nums, dp, target - nums[i], i + 1):
                    dp[i][target] = True
                    return True

            # recursive call after excluding the number at the i
            dp[i][target] = self.helper(nums, dp, target, i + 1)

        return dp[i][target]

# The above algorithm has time and space complexity of O(N*S), where ‘N’
# represents total numbers and ‘S’ is the total sum of all the numbers.
