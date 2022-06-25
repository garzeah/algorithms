class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        # If 'target' is a an odd number, we can't have two subsets with equal target
        if target % 2 == 1:
            return False

        return self.helper(nums, target / 2, 0)


    def helper(self, nums, target, i):
        # Base case
        if target == 0:
            return True

        if target < 0 or i >= len(nums):
            return False

        # Decision to see if any of the numbers will equal our target
        if nums[i] <= target:
            if self.helper(nums, target - nums[i], i + 1):
                return True

        # Decision to see if any of the values is equal to our target
        return self.helper(nums, target, i + 1)

# The time complexity of the above algorithm is exponential O(2^n), where ‘n’ 
# represents the total number. The space complexity is O(n), this memory
# which will be used to store the recursion stack.
