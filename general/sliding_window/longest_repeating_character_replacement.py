# Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, max_repeat, max_length = 0, 0, 0;
        freq_map = {};

        for end in range(len(s)):
            right_elem = s[end]

            if right_elem not in freq_map:
                freq_map[right_elem] = 0

            freq_map[right_elem] += 1
            max_repeat = max(max_repeat, freq_map[right_elem])

            # If we take the length - the most frequent character,
            # this will give us the amount of characters we can replace
            while ((end - start + 1 - max_repeat) > k):
                left_elem = s[start]
                freq_map[left_elem] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length

# Time Complexity: O(n)
# Space Complexity: O(1), max amt of chars we can store is
# O(26) cuz of alphabet which is essential O(1)