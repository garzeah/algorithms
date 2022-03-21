class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x1, x2 = 1, nums[0]

        # x1 represents XOR of all values from 1 to n
        for i in range(2, len(nums) + 1): # len(nums) + 1 bc end range is exclusive
            x1 = x1 ^ i

        # x2 represents XOR of all values in nums
        for i in range(1, len(nums)):
            x2 = x2 ^ nums[i]

        return x1 ^ x2

# Time Complexity: O(n)
# Space Complexity: O(1)