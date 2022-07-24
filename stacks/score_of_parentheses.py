class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0 # multiplier for nested parentheses

        # Everytime we encounter '(', we will append a score of 0.
        # Then when we encounter ')', we will add the current
        # score with our multiplier max(1, score * 2)
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            elif char == ')':
                score = stack.pop() + max(1, score * 2) # multiplier

        return score

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/score-of-parentheses/discuss/1856451/Beginner-friendly-python-solution