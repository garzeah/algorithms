class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        curr_path = set() # Since we don't revisit the same pos

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or # Out of bounds
                r >= rows or c >= cols or # Out of bounds
                word[i] != board[r][c] or # Not matching
                (r, c) in curr_path): # Already visited
                return False

            curr_path.add((r, c))

            # Running dfs in all 4 adjacent positions
            res = (dfs(r + 1, c, i + 1) or # Down
                   dfs(r - 1, c, i + 1) or # Up
                   dfs(r, c + 1, i + 1) or # Right
                   dfs(r, c - 1, i + 1)) # Left

            # Remove the position we just added to the path
            # since we are no longer visiting that position
            curr_path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

# Time Complexity: O(n * m * 4^n) where n is the number of columns
# and m in the number of rows. For some positions, we will have
# at most 4 possible choices to backtrack from.

# Space Complexity: O(1) since we are just returning a bool value.

# Solution: https://www.youtube.com/watch?v=pfiQ_PS1g8E
