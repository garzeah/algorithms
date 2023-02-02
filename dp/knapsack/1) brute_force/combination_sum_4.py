class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0)

    def helper(self, nums, target, i):
        if target == 0:
            return 1

        if target < 0 or i >= len(nums):
            return 0

        count1 = 0
        if nums[i] <= target:
            count1 += self.helper(nums, target - nums[i], 0)

        count2 = self.helper(nums, target, i + 1)

        return count1 + count2