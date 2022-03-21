class Solution:
    def isValid(self, s: str) -> bool:
        # Creating a close to open map to see if our char is in there
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for char in s:
            if char in close_to_open:
                # Want to check if we have a stack, and if the last value
                # of the list contains the matching bracket. We did a
                # mapping of close to open bc we'll have left opening
                # parentheses in our stack to check for
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            # Adding the left open characters in
            else:
                stack.append(char)

        return len(stack) == 0

# Time Complexity: O(n)
# Space Complexity: O(n)