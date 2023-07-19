class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs:
            while word.startswith(prefix) is False:
                prefix = prefix[:-1]

        return prefix

# TC: O(n^2)
# SC: O(1)