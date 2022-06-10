class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()

        # For every character, we want to collect the remaining odds only
        for char in s:
            if char not in char_set:
                char_set.add(char)
            else:
                char_set.remove(char)

        # If we have an odd remaining, we only can use 1
        # to build the longest palindrome
        if len(char_set) != 0:
            return len(s) - len(char_set) + 1
        # The whole string is a palindrome
        else:
            return len(s)

# Time Complexity: O(n)
# Space Complexity: O(26) since we can only have unique characters which is essentially O(1)
# Solution: https://leetcode.com/problems/longest-palindrome/discuss/813721/Python-3-solution-using-Set()