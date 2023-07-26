class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]

        for word in strs:
            while word.startswith(lcp) is False:
                lcp = lcp[:-1]

        return lcp

# TC: O(n^2)
# SC: O(1)
