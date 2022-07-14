class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }
        curr_path, res = [], []
        return self.backtrack(digits, digit_to_char, 0, curr_path, res)

    def backtrack(self, digits, digit_to_char, start, curr_path, res):
        if len(curr_path) == len(digits):
            res.append("".join(curr_path))
            return

        letters = digit_to_char[digits[start]]
        for char in letters:
            curr_path.append(char)
            self.backtrack(digits, digit_to_char, start + 1, curr_path, res)
            curr_path.pop()

        return res

# Time Complexity: O(N * 4^N) because worst case, we'll have to perform
# backtracking on a number that contains 4 characters which will
# exponentially increase our res.

# Space Complexity: O(N * 4^N) because worst case, we'll have to perform
# backtracking on a number that contains 4 characters which will
# exponentially increase our res.

# Solution: https://www.youtube.com/watch?v=0snEunUacZY