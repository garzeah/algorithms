class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')

        for i in range(len(nums)):
            curr = nums[i]
            max_product = max(max_product, curr)
            for j in range(i + 1, len(nums)):
                curr *= nums[j]
                max_product = max(max_product, curr)

        return max_product

# Time Complexity: O(n^2)
# Space Complexity: O(1)