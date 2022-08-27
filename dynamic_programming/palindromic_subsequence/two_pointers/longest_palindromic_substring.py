class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        start, end = 0, 0

        # As we iterate through each letter in our string, we want
        # to check if the letters to the left and right are equal
        # and record the longest palindrome. This would improve
        # optimization a lot because the brute force way would
        # be to check the longest palindrome for each subarray
        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Record the new max length and its positions
                if (r - l + 1) > max_length:
                    start = l
                    end = r
                    max_length = r - l + 1
                l -= 1
                r += 1

            # Even Length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Record the new max length and its positions
                if (r - l + 1) > max_length:
                    start = l
                    end = r
                    max_length = r - l + 1
                l -= 1
                r += 1

        return s[start:end + 1]

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=XYQecbcd6_c