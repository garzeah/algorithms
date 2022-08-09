class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        mult = 0 # multiplier for nested parentheses

        # Everytime we encounter '(', we will append a mult of 0.
        # Then when we encounter ')', we will add the current
        # mult with our multiplier max(1, mult * 2)
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