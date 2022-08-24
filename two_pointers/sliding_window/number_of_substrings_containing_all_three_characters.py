class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start, count = 0, 0
        freq = { char: 0 for char in 'abc' }

        for end in range(len(s)):
            right_char = s[end]
            freq[right_char] += 1

            while freq['a'] and freq['b'] and freq['c']:
                left_char = s[start]
                freq[left_char] -= 1
                start += 1

            count += start

        return count

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/1521816/Python-Sliding-Window-Solution-with-Explanation