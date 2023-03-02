class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        res = 0
        for i in range(2, len(nums)):
            for j in range(i, len(nums)):
                # For every arithmetic we find, we want to increment our result
                if nums[j - 1] - nums[j] == nums[j - 2] - nums[j - 1]:
                    res += 1
                # Check next pair of 3 numbers
                else:
                    break

        return res

# Time Complexity: O(n^2)
# Time Complexity: O(1)