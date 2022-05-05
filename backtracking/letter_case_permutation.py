class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        curr_path, output = [], []
        return self.backtrack(s, 0, curr_path, output)

    def backtrack(self, s, i, curr_path, output):
        if len(curr_path) == len(s):
            output.append("".join(curr_path))
        else:
            if s[i].isalpha():
                curr_path.append(s[i].swapcase())
                self.backtrack(s, i + 1, curr_path, output)
                curr_path.pop()

            curr_path.append(s[i])
            self.backtrack(s, i + 1, curr_path, output)
            curr_path.pop()

        return output

# Time Complexity: O(N * 2^N) where N is the amount of alpha-characters in a string.
# Per each character, we have 2 choices which is lower and upper case.

# Space Complexity: O(N * 2^N) where N is the amount of alpha-characters in a string.
# Per each character, we have 2 choices which is lower and upper case.

# Solution: https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution