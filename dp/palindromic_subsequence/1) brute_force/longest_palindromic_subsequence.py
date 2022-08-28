class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.helper(s, 0, len(s) - 1)

    def helper(self, s, left, right) -> int:
        if left > right:
            return 0

        if left == right:
            return 1

        res = 0

        if s[left] == s[right]:
            res = 2 + self.helper(s, left + 1, right - 1)
        else:
            res = max(self.helper(s, left + 1, right), self.helper(s, left, right - 1))

        return res

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Solution: https://leetcode.com/problems/longest-palindromic-subsequence/discuss/1266203/Memo-oror-DP-2-D-array-oror-DP-1-D-array