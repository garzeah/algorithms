class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        curr_path, output = "", []
        self.backtrack(digits, digit_to_char, 0, curr_path, output)
        return output

    def backtrack(self, digits, digit_to_char, i, curr_path, output):
        # We were able to take every single digit and map it to a character
        if len(curr_path) == len(digits):
            output.append(curr_path)
            return

        # For every number in our input, we are going to recursively add a
        # character that follows the digit_to_char mapping
        for char in digit_to_char[digits[i]]:
            self.backtrack(digits, digit_to_char, i + 1, curr_path + char, output)


# Time Complexity: O(N * 4^N) becase the max amount of
# digits is 4 and for every number in N, there are
# 4 possible choices.

# Space Complexity: O(N * 4^N) because out output
# will grow at a rate of 4^N since each digit
# has 4 possible choices to choose from.

# Solution: https://www.youtube.com/watch?v=0snEunUacZY