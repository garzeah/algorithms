class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Want to use a monotonic decreasing stack to find NGE (next greater element).
        # In the first loop, we fill NGE all possible.
        stack, res = [], [-1] * len(nums)
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(i)

        # In the second loop, there might be some elements left in the stack, so we
        # iterate again (without appending to stack) and get NGE. The elements that
        # are left in the stack even after second loop are max(nums).
        for num in nums:
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num

        return res

# Time Complexity: O(N)
# Space Complexity: O(N)
# Solution: https://leetcode.com/problems/next-greater-element-ii/discuss/703473/Python-Simple-2-pass-solution-using-stack-99-faster