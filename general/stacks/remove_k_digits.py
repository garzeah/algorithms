class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # When numbers are in increasing order, we want
        # to remove the last digits

        # When numbers are in decreasing order, we want
        # to remove the first digits

        stack = []
        for n in num:
            # While we have a stack, it is in decreasing order
            # and we can still remove values, we want to
            # remove the first digits
            while stack and int(stack[-1]) > int(n) and k:
                stack.pop()
                k -= 1

            stack.append(n)

        # For the remaining k, we will have increasing
        # order left so we want to remove the last digits
        while k:
            stack.pop()
            k -= 1

        # Removing leading zeroes
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1

        return ''.join(stack[i:]) if len(stack[i:]) > 0 else "0"

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/remove-k-digits/discuss/700059/Python-Very-detail-explanation-with-examples-using-stack