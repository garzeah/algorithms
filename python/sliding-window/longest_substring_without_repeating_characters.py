# Longest Substring without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_length, index_map = 0, 0, {}

        for end in range(len(s)):
            right_char = s[end]

            # if the map already contains the 'right_char', shrink the window from the beginning so that
            # we have only one occurrence of 'right_char'
            if right_char in index_map:
                # this is tricky; in the current window, we will not have any 'right_char' after its previous index
                # and if 'start' is already ahead of the last index of 'right_char', we'll keep 'start'
                start = max(start, index_map[right_char] + 1)

            # insert the index into our map and calculate the max length
            index_map[right_char] = end
            max_length = max(max_length, end - start + 1)

        return max_length
