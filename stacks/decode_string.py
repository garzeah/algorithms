class Solution:
    def decodeString(self, s: str) -> str:
        # We can use a stack to deal with the calculations of
        # of each number and character. This helps especially
        # when dealing with nested brackets because we could
        # use a stack to calculated the nested brackets first
        # then the outer brackets
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                # Want to get all the substrs contained in a bracket
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # Popping opening bracket

                # Want to get the number to multiply with
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # May be more than 1 digit

                stack.append(int(k) * substr) # Multiplying the string and adding it back

        return "".join(stack)

# Time Complexity: O(n) where n is the amount of characters in s
# Space Complexity: O(n) where n is the amount of characters in s
# Solution: https://www.youtube.com/watch?v=qB0zZpBJlh8