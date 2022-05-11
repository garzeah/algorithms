class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        curr_path = set() # Since we don't revisit the same pos

        def dfs(row, col, i):
            if i == len(word):
                return True

            if (
                row < 0 or col < 0 or # Out of bounds
                row >= rows or col >= cols or # Out of bounds
                word[i] != board[row][col] or # Not matching
                (row, col) in curr_path # Already visited
            ):
                return False


            curr_path.add((row, col))

            # Check adjacent positions for our word
            output = (
                dfs(row + 1, col, i + 1) or # Right
                dfs(row - 1, col, i + 1) or # Left
                dfs(row, col + 1, i + 1) or # Up
                dfs(row, col - 1, i + 1) # Down
            )

            curr_path.remove((row, col))

            return output

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False

# Time Complexity: O(n * m * 4^n) where n is the number of columns
# and m in the number of rows. For some positions, we will have
# at most 4 possible choices to backtrack from.

# Space Complexity: O(1) since we are just returning a bool value.

# Solution: https://www.youtube.com/watch?v=pfiQ_PS1g8E
