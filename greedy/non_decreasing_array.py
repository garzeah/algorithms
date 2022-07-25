class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0 # Keep track of the times we need to modify

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
                if count > 1:
                    return False

                # Need to add this check in because [3,4,2,3] gets marked as a
                # false positive since we only count 1 violation. A way to fix
                # this is whenever we encounter a violation, we can can check
                # 2 positions back and check if it is greater than the current
                # value since it is in increasing order. Then we can replace
                # the current value with the previous to throw of false positive.
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]

        return True

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/non-decreasing-array/discuss/2193030/Python-Easy-Greedy-w-explanation-O(1)-space