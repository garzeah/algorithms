# Permutation in String
class Solution:
    def checkInclusion(self, pattern: str, str1: str) -> bool:
        start, matched = 0, 0
        pattern_freq = {}

        # recording the frequency of each character in the pattern
        for char in pattern:
            if char not in pattern_freq:
                pattern_freq[char] = 0
            pattern_freq[char] += 1

        # our goal is to match all the characters from the 'pattern_freq' with
        # the current window try to extend the range [start, end]
        for end in range(len(str1)):
            right_char = str1[end]

            if right_char in pattern_freq:
                # decrement the frequency of matched character
                pattern_freq[right_char] -= 1

                if pattern_freq[right_char] == 0:
                    matched += 1

            # Means we have eaxctly matched the pattern
            if matched == len(pattern_freq):
                return True

            # Pattern bc pattern_freq could be 1 if
            # if we get an input like "aaaaaaaaaaa"
            if end >= len(pattern) - 1:
                left_char = str1[start]
                start += 1
                # "reseting" the conditions for our
                # current window to see if is a permutation
                if left_char in pattern_freq:
                    if pattern_freq[left_char] == 0:
                        matched -= 1
                    pattern_freq[left_char] += 1
        return False

# Time Complexity
# is O(N + M) where N and M are the number of
# characters in the input strings

# Space Complexity
# is O(M) b/c the worst case is that the pattern
# has a distinct amount of characters