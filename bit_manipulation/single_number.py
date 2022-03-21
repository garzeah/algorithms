class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = nums[0]

        # The duplicate values will cancel each other out
        # when you perform the xor operator on them
        for i in range(1, len(nums)):
            x1 = x1 ^ nums[i]

        return x1

# Time Complexity: O(n)
# Space Complexity: O(1)