class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordSet = set(wordDict)
        memo = {}

        def helper(substr):
            # Base case, if the substr has been
            # memoized, return that value
            if substr in memo:
                return memo[substr]

            res = []
            for i in range(len(substr)):
                prefix = substr[:i + 1] # Get every char up to i + 1

                # Want to check if prefix is in our word set
                if prefix in wordSet:
                    # If prefix is equal to our substr then we can append
                    # the prefix for our particular substr
                    if prefix == substr:
                        res.append(prefix)
                    # Otherwise, we want to perform recursion on the remaining characters
                    # and for the words we get back from our cache, we want to build
                    # the valid phrases
                    else:
                        restOfWord = helper(substr[i+1:])
                        for word in restOfWord:
                            res.append(prefix + ' ' + word)

            memo[substr] = res
            return res

        return helper(s)

# Solution:
    # - https://www.youtube.com/watch?v=hRqJJF2j3To
    # - https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution/119968