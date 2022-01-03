# Minimum Window Substring
class Solution:
    def minWindow(self, str1: str, pattern: str) -> str:
        window_start, matched, substr_start = 0, 0, 0
        min_length = float('inf')
        pattern_freq = {}

        for chr in pattern:
            if chr not in pattern_freq:
                pattern_freq[chr] = 0
            pattern_freq[chr] += 1

        # try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in pattern_freq:
                pattern_freq[right_char] -= 1
                if pattern_freq[right_char] >= 0:  # Count every matching of a character
                    matched += 1

            # Shrink the window if we can, finish as soon as we remove a matched character
            while matched == len(pattern):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start

                left_char = str1[window_start]
                window_start += 1
                if left_char in pattern_freq:
                    # Note that we could have redundant matching characters, therefore we'll decrement the
                    # matched count only when a useful occurrence of a matched character is going out of the window
                    if pattern_freq[left_char] == 0:
                        matched -= 1
                    pattern_freq[left_char] += 1

        if min_length > len(str1):
            return ""

        return str1[substr_start:substr_start + min_length]

# Time Complexity: O(N + M) where N and M are the number of characters
# in the input string.

# Space Complexity: O(M) where it is the size of pattern that we take up
# in pattern_freq