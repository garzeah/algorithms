class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def helper(substr):
            if substr in memo:
                return memo[substr]

            res = []
            for i in range(len(substr)):
                prefix = substr[:i + 1]

                # Want to check if the prefix is in our word set
                if prefix in word_set:
                    # We found our word so add it to our result
                    if prefix == substr:
                        res.append(prefix)
                    # If it doesn't equal our substring (e.g our input is catsanddog and
                    # we have cat but not sanddog) then we want to loop through the rest
                    # of the substring and for each phrase we get back, add to result
                    else:
                        rest_of_words = helper(substr[i+1:])
                        for phrase in rest_of_words:
                            res.append(prefix + ' ' + phrase)

            memo[substr] = res
            return res

        return helper(s)

# Solution:
    # - https://www.youtube.com/watch?v=hRqJJF2j3To
    # - https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution/119968