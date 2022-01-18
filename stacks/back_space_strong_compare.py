class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def handleBackspace(s):
            stack = []

            for char in s:
                # Push new char into stack
                if char != '#':
                    stack.append(char)
                elif stack and char == '#':
                # Pop last char from stack, as a result of '#'
                    stack.pop()

            return ''.join(stack)

        return handleBackspace(s) == handleBackspace(t)

# Time Complexity: O(n)
# Space Complexity: O(n)