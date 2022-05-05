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
        curr_path, output = [], []
        return self.backtrack(digits, digit_to_char, 0, curr_path, output)

    def backtrack(self, digits, digit_to_char, i, curr_path, output):
        if len(curr_path) == len(digits):
            output.append("".join(curr_path))
            return

        for char in digit_to_char[digits[i]]:
            curr_path.append(char)
            self.backtrack(digits, digit_to_char, i + 1, curr_path, output)
            curr_path.pop()

        return output

# Time Complexity: O(N * 4^N) because worst case, we'll have to perform
# backtracking on a number that contains 4 characters which will
# exponentially increase our output.

# Space Complexity: O(N * 4^N) because worst case, we'll have to perform
# backtracking on a number that contains 4 characters which will
# exponentially increase our output.

# Solution: https://www.youtube.com/watch?v=0snEunUacZY