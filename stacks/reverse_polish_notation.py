class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # We can use a stack to perform calculations on
        # the previous numbers and whenever we encounter
        # an operator, we can perform those calculations
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a, b = stack.pop(), stack.pop()
                # Converts to int and rounds toward 0
                stack.append(int(b / a))
            else:
                stack.append(int(char))

        return stack[0]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=iu0082c4HDE