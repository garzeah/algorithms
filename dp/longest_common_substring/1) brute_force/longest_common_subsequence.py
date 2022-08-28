class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        return self.helper(text1, text2, 0, 0)

    def helper(self, s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return 0

        if s1[i] == s2[j]:
            return 1 + self.helper(s1, s2, i + 1, j + 1)

        c1 = self.helper(s1, s2, i + 1, j)
        c2 = self.helper(s1, s2, i, j + 1)

        return max(c1, c2)

# Time Complexity: O(2^(m + n))
# Space Complexity: O(n + m)
# Solution: Grokking