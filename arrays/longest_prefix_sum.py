class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs:
            # Whenever we don't have a match, we are going to
            # remove a letter from the end until we get the
            # longest common prefix
            while word.startswith(prefix) is False:
                prefix = prefix[:-1]

        return prefix

# Time Complexity: O(n*m) where n is the amount of words and m
# is the max length of all words

# Space Complexity: O(m) where m is the max length of all words