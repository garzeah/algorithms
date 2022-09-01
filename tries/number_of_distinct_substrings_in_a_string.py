class Solution:
    def countDistinct(self, s: str) -> int:
        trie, res = {}, 0

        # For every character in i, we want to intialize a
        # trie and for every char j between i and len(s),
        # we will begin building building our trie
        for i in range(len(s)):
            curr = trie
            for j in range(i, len(s)):
                # If the character doesn't exist in our trie,
                # we want to build connections with the new char
                if s[j] not in curr:
                    curr[s[j]] = {}
                    res += 1 # Each new connection is a distinct subtring

                curr = curr[s[j]] # Moving our pointer up

        return res

# Time Complexity: O(n^2)
# Space Complexity: O(n^2) as an upperbound since we the number of
# distinct characters can exceed O(n)
# Solution: https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/discuss/984839/9-lines-Trie-with-python