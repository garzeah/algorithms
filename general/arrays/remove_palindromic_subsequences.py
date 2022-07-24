class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s is None:
            return 0

        # Since we only have 2 characters max, we will only need
        # 2 operations at most. For example, one to remove all
        # of 'a' and 1 to remove all of 'b'.
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return 2

            l += 1
            r -= 1

        # Whole string is a palindrome
        return 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=M8gA5JOopLw