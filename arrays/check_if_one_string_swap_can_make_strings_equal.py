class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        freq1, freq2 = Counter(s1), Counter(s2)
        for key in freq1:
            if freq1[key] != freq2[key] or key not in freq2:
                return False

        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1

            if count > 2:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/discuss/1899557/Very-Easy-to-understand-PYTHON