class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            # If we have a stack, the prior value in the stack matches the
            # parentheses type and it is a closing parentheses, then we pop
            if stack and stack[-1] == close_to_open[char] and char in close_to_open:
                stack.pop()
            else:
                stack.append(char)

        # Assuming we have valid parentheses, the length would equal 0
        return len(stack) == 0

# Time Complexity: O(n)
# Space Complexity: O(n)