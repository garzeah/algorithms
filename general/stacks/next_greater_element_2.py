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
            # If there is a number that is higher than the last value
            # of the stack, then we want to pop those number(s) and
            # add the new one in. When we pop those numbers, the
            # current number will be the NGE. We store num and i
            # in our stack to compare w/ the current number and
            # if we pop, to mark the NGE
            while stack and num > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = num
            stack.append((num, i))

        for num in nums:
            # Since it's circular, we want to go around again and do the same
            # thing as above in case any number that came before the last
            # number could be the NGE
            while stack and num > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = num

        return res

# Time Complexity: O(N)
# Space Complexity: O(N)
# Solution: https://leetcode.com/problems/next-greater-element-ii/discuss/703473/Python-Simple-2-pass-solution-using-stack-99-faster