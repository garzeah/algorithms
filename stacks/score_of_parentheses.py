class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        mult = 0 # multiplier for nested parentheses

        # Every time we encounter '(', we want to add the current iteration's
        # multiplicity to our stack and reset it. When we encounter ')' we
        # can built off of each multiplicity by adding the last value
        # with max(1, mult * 2)
        # ((())) = [0, 0, 0]
        # [0, 0]; mult = 1
        # [0]; mult = 2
        # []; mult = 4
        for char in s:
            if char == '(':
                stack.append(mult) # Cumulation of each level
                mult = 0 # Reset the multiplier
            elif char == ')':
                mult = stack.pop() + max(1, mult * 2) # multiplier

        return mult

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/score-of-parentheses/discuss/1856451/Beginner-friendly-python-solution