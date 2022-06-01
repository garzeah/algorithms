class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col):
            board[row][col] = "T"
            for x, y in directions:
                r, c = row + x, col + y

                if (
                    r in range(ROWS) and
                    c in range(COLS) and
                    board[r][c] == "O"
                ):
                    dfs(r, c)

        # Capture the unsurrounded regions (O -> T)
        # by performing DFS on the borders and for
        # each O, set to T since it is unsurrounded
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    (row in [0, ROWS - 1] or col in [0, COLS - 1]) and
                    board[row][col] == "O"
                ):
                    dfs(row, col)

        # Capture the surrounded regions (O -> X)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"

        # Uncapture the unsurrounded regions (T -> O)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Solution: https://www.youtube.com/watch?v=9z2BunfoZ5Y