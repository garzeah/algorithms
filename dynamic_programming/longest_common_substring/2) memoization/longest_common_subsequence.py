class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[-1 for x in range(len(text2))] for y in range(len(text1))]
        return self.helper(text1, text2, dp, 0, 0)

    def helper(self, s1, s2, dp, i, j):
        if i == len(s1) or j == len(s2):
            return 0

        if dp[i][j] == -1:
            if s1[i] == s2[j]:
                return 1 + self.helper(s1, s2, dp, i + 1, j + 1)

            c1 = self.helper(s1, s2, dp, i + 1, j)
            c2 = self.helper(s1, s2, dp, i, j + 1)

            dp[i][j] = max(c1, c2)

        return dp[i][j]

# Time Complexity: O(n * m)
# Space Complexity: O(n * m) + O(n + m)
# Solution: Grokking