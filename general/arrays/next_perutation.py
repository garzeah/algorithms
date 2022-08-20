class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We want to find the point where the numbers stop decreasing
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        # If all numbers are in decreasing order, there is no next perm.
        if i == 0:
            nums.reverse()
            return

        # Find the last "ascending" position in the decreasing range
        k = i - 1
        while nums[k] >= nums[j]:
            j -= 1

        # When we find the last "ascending" then we want to swap
        # and reverse the decreasing portion
        nums[k], nums[j] = nums[j], nums[k]

        l, r = k + 1, len(nums) - 1  # Reverse the decreasing portion
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -= 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution:
#   - https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
#   - https://www.youtube.com/watch?v=quAS1iydq7U