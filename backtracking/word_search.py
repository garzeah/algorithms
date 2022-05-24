class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        curr_path = set() # Since we don't revisit the same pos

        def backtrack(row, col, i):
            # Base case for when we find the word. This
            # has to be on top because we want to check
            # if we have a matching word first before
            # it is out of bounds.
            if i == len(word):
                return True

            # Base case for when we don't find the word
            if (
                row < 0 or row >= ROWS or # Out of bounds
                col < 0 or col >= COLS or # Out of bounds
                (row, col) in curr_path or # Already visited
                board[row][col] != word[i] # Not matching
            ):
                return False


            curr_path.add((row, col))

            # Checking adjacent positions for our word
            output = (
                backtrack(row + 1, col, i + 1) or # Bottom
                backtrack(row - 1, col, i + 1) or # Top
                backtrack(row, col + 1, i + 1) or # Right
                backtrack(row, col - 1, i + 1) # Left
            )

            curr_path.remove((row, col))

            return output

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True

        return False

# Time Complexity: O(n * m * 4^n) where n is the number of columns
# and m in the number of ROWS. For some positions, we will have
# at most 4 possible choices to backtrack from.

# Space Complexity: O(1) since we are just returning a bool value.

# Solution: https://www.youtube.com/watch?v=pfiQ_PS1g8E
