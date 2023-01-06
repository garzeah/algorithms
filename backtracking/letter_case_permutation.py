class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        return self.backtrack(s, 0, [], res)

    def backtrack(self, s, i, curr_path, res):
        if len(curr_path) == len(s):
            res.append("".join(curr_path))
            return

        if s[i].isalpha():
            curr_path.append(s[i].swapcase())
            self.backtrack(s, i + 1, curr_path, res)
            curr_path.pop()

        curr_path.append(s[i])
        self.backtrack(s, i + 1, curr_path, res)
        curr_path.pop()

        return res

# Time Complexity: O(N * 2^N) where N is the amount of alpha-characters in a string.
# Per each character, we have 2 choices which is lower and upper case.

# Space Complexity: O(N * 2^N) where N is the amount of alpha-characters in a string.
# Per each character, we have 2 choices which is lower and upper case.

# Solution: https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution