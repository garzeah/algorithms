class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        curr = 0 # Keep track of continual slices
        res = 0

        for i in range(2, len(nums)):
            # For every arithmetic we find, we want to increment our result
            if nums[i - 1] - nums[i] == nums[i - 2] - nums[i - 1]:
                curr += 1 # Keep incrementing each new slice we find by 1
                res += curr
            else: # If it's not a continual slice
                curr = 0

        return res

# Time Complexity: O(n)
# Time Complexity: O(1)