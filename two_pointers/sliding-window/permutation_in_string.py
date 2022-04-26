# Permutation in String
class Solution:
    def checkInclusion(self, pattern: str, s: str) -> bool:
        start, matched = 0, 0
        freq_map = Counter(pattern)

        # Our goal is to match all the characters from the 'freq_map' with
        # the current window try to extend the range [start, end]
        for end in range(len(s)):
            right_char = s[end]

            # Checking if the end of the window has a match
            if right_char in freq_map:
                freq_map[right_char] -= 1
                if freq_map[right_char] == 0:
                    matched += 1

            # Means we have eaxctly matched the pattern
            if matched == len(freq_map):
                return True

            # Has to be at least this long before we start sliding the window
            if end >= len(pattern) - 1:
                left_char = s[start]
                start += 1

                # Sliding the window
                if left_char in freq_map:
                    if freq_map[left_char] == 0:
                        matched -= 1
                    freq_map[left_char] += 1
        return False

# Time Complexity
# is O(N + M) where N and M are the number of
# characters in the input strings

# Space Complexity
# is O(M) b/c the worst case is that the pattern
# has a distinct amount of characters