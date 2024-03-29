class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        return self.helper(s, word_set)

    def helper(self, substr, word_set):
        res = []
        for i in range(len(substr)):
            # Want to get every possible substring
            prefix = substr[:i + 1]

            # Want to check if the prefix is in our word set
            if prefix in word_set:
                # We found our word so and it matches our substr
                # so we want to continue building off that to
                # form possible sentences
                if prefix == substr:
                    res.append(prefix)
                # If it doesn't equal our substring (e.g our input is catsanddog and
                # we have cat but not sanddog) then we want to loop through the rest
                # of the substring and for each phrase we get back, add to result.
                # In the event we do have a prefix, want to continue looking
                # for other matches to form our sentence
                else:
                    rest_of_words = self.helper(substr[i+1:], word_set)
                    for phrase in rest_of_words:
                        res.append(prefix + ' ' + phrase)

        return res

# Solution:
    # - https://www.youtube.com/watch?v=hRqJJF2j3To
    # - https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution/119968