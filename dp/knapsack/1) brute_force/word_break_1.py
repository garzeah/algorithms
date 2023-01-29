class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        return self.helper(s, wordDict)

    def helper(self, s, wordDict):
        # If the word is empty its in wordDict or we've
        # stripped  off every word and result is empty
        if len(s) == 0:
            return True

        for word in wordDict:
            # Check if any words in dictionary are in the beginning of s
            prefix = s[0:len(word)]

            # If we found a match, recursive call with that part stripped off
            if prefix == word and self.helper(s[len(word):], wordDict):
                return True

        return False

# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Solution:
# - https://leetcode.com/problems/word-break/discuss/1017085/Simple-Python-Solution-w-Memoization
# - https://www.youtube.com/watch?v=Sx9NNgInc3A