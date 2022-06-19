class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tuples = zip(*strs) # Returns a tuple pair of letters of all words
        res = ""

        for tup in tuples:
            if len(set(tup)) > 1: # Letters do not match
                break
            else: # Otherwise they do and add to our result
                res += tup[0]

        return res

# Time Complexity: O(n * m) where n is the amount of words in the array
# and m is the smallest word length we have in our array.

# Space Complexity: O(n * m) where n is the amount of words in the array
# and m is the smallest word length we have in our array.

# Solution: https://leetcode.com/problems/longest-common-prefix/discuss/354496/Python3-list(zip(*str))

