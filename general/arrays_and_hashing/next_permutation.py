class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the longest decreasing sequence of numbers and mark it
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # If all numbers are in decreasing order, there is no next perm.
        if i == 0:
            nums.reverse()
            return

        # Mark our pivot which is the value before the decreasing sequence
        # and find the rightmost successor to our pivot in the sequence
        k = i - 1
        while j >= 0 and nums[k] >= nums[j]:
            j -= 1

        # Swap with pivot
        nums[k], nums[j] = nums[j], nums[k]

        # Reverse the decreasing sequence
        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -= 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution:
#   - https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
#   - https://www.youtube.com/watch?v=quAS1iydq7U