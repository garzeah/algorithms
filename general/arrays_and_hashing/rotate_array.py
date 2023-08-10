class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # Ensuring that we don't rotate outside the array

        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        helper(0, len(nums) - 1) # Reverse the array
        helper(0, k - 1) # Reverse up to k
        helper(k, len(nums) - 1) # Reverse from k to last number

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=BHr381Guz3Y

