class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.helper(s, dp, 0, len(s) - 1)

    def helper(self, s, dp, left, right) -> int:
        if left > right:
            return 0

        if left == right:
            return 1

        if dp[left][right] == -1:
            res = 0

            if s[left] == s[right]:
                res = 2 + self.helper(s, dp, left + 1, right - 1)
            else:
                res = max(self.helper(s, dp, left + 1, right), self.helper(s, dp, left, right - 1))

            dp[left][right] = res

        return dp[left][right]

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Solution: https://leetcode.com/problems/longest-palindromic-subsequence/discuss/1266203/Memo-oror-DP-2-D-array-oror-DP-1-D-array