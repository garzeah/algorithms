class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

        # For each character, if we encount an opening
        # parentheses then we want to add the index of
        # if to our stack. When we encounter a closing
        # parentheses, we have 2 choices, if our stack
        # still has opening parentheses, then we can
        # pop from our stack. If we do not, then we
        # can set that closing parentheses to 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack: # Removing opening bracket
                    stack.pop()
                else: # Assign remaining closing bracket to empty string
                    s[i] = ""

        # For all the remaining opening parentheses in
        # our stack, we can assign to an empty string
        for i in stack:
            s[i] = ""

        return "".join(s)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=FTo1kDyE-h4