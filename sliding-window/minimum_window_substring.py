# Minimum Window Substring
class Solution:
    def minWindow(self, s: str, pattern: str) -> str:
        start, matched, substr_start = 0, 0, 0
        min_length = float('inf')
        pattern_freq = {}

        for char in pattern:
            if char not in pattern_freq:
                pattern_freq[char] = 0
            pattern_freq[char] += 1

        for end in range(len(s)):
            right_char = s[end]

            if right_char in pattern_freq:
                pattern_freq[right_char] -= 1
                if pattern_freq[right_char] >= 0:
                    matched += 1

            # Shrink the window if we can, finish as soon as we remove a matched character
            # Don't want to use pattern_freq since it can have more than pattern
            # since we are finding the minimum window substring
            while matched == len(pattern):
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    substr_start = start

                left_char = s[start]
                start += 1

                if left_char in pattern_freq:
                    # Note that we could have redundant matching characters, therefore we'll decrement the
                    # matched count only when a useful occurrence of a matched character is going out of the window
                    if pattern_freq[left_char] == 0:
                        matched -= 1
                    pattern_freq[left_char] += 1

        if min_length > len(s):
            return ""

        return s[substr_start:substr_start + min_length]


# Time Complexity: O(N + M) where N and M are the number of characters
# in the input string.

# Space Complexity: O(M) where it is the size of pattern that we take up
# in pattern_freq