class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Want to convert smaller numbers in front of a
        # larger number so it is easier to translate
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        res = 0
        for char in s:
            res += translations[char]

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/roman-to-integer/discuss/264743/Clean-Python-beats-99.78.