class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        # if 's' is a an odd number, we can't have two subsets with equal sum
        if s % 2 != 0:
            return False

        return self.helper(nums, s / 2, 0)


    def helper(self, nums, sum, idx):
        # Base case
        if sum == 0:
            return True

        if len(nums) == 0 or idx >= len(nums):
            return False

        # Recursive call after choosing the number at the `idx`
        # if the number at `idx` exceeds the sum, we shouldn't process this
        if nums[idx] <= sum:
            if(self.helper(nums, sum - nums[idx], idx + 1)):
                return True

        # Recursive call after excluding the number at the 'idx'
        return self.helper(nums, sum, idx + 1)