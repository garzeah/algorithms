class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        operator, i, res = 1, 0, 0

        # Check for whitespace
        while i < len(s) and s[i] == ' ':
            i += 1

        # Check for plus or minus operator
        if i < len(s) and s[i] == '-':
            i += 1
            operator = -1

        elif i < len(s) and s[i] == '+':
            i += 1

        # Check if the number is between 0-9
        checker = set('0123456789') # Can use a set for O(1) lookup

        while i < len(s) and s[i] in checker:
            # Building out the result and casting to an int
            res = res * 10 + int(s[i])
            i += 1

        res = res * operator # Determining whether positive or negative

        # Clamping the integer so it remains in range
        return max(res, MIN_INT) if res < 0 else min(res, MAX_INT)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=zwZXiutgrUE