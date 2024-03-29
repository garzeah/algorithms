class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set, dp = set(wordDict), {}
        return self.helper(s, word_set, dp)

    def helper(self, s, word_set, dp):
        # If the word is empty its in wordDict or we've
        # stripped  off every word and result is empty
        if len(s) == 0:
            return True

        if s in dp:
            return dp[s]

        for word in word_set:
            # Check if any words in dictionary are in the beginning of s
            prefix = s[0:len(word)]

            # If we found a match, recursive call with that part stripped off
            if prefix == word and self.helper(s[len(word):], word_set, dp):
                dp[prefix] = True
                return dp[prefix]

        dp[s] = False
        return dp[s]

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Solution:
# - https://leetcode.com/problems/word-break/discuss/1017085/Simple-Python-Solution-w-Memoization
# - https://www.youtube.com/watch?v=Sx9NNgInc3A