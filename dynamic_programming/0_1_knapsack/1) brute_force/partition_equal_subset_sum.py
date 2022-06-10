class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        # If 'target' is a an odd number, we can't have two subsets with equal target
        if target % 2 == 1:
            return False

        return self.helper(nums, target / 2, 0)


    def helper(self, nums, target, idx):
        # Base case
        if target == 0:
            return True

        if len(nums) == 0 or idx >= len(nums):
            return False

        # Recursive call after choosing the number at the `idx` if the
        # number at `idx` exceeds the target, we shouldn't process this
        if nums[idx] <= target:
            if self.helper(nums, target - nums[idx], idx + 1):
                return True

        # Recursive call after excluding the number at the 'idx'
        return self.helper(nums, target, idx + 1)