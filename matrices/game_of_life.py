class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Keeping a map of the original and new values because when changing
        # the state, we want to depend on the original values rather than new
        # Original | New | State
        #    0     |  0  |   0   # Nothing changes
        #    1     |  0  |   1   # Cell that dies when neigbhors are < 2 or > 3
        #    0     |  1  |   2   # Becomes a live cell w/ exactly 3 neighbors
        #    1     |  1  |   3   # Cell with 2 or 3 neighbors gets to live on

        ROWS, COLS = len(board), len(board[0])

        def count_neighbors(row, col):
            directions = [
                [1,0],[-1,0],[0,1],[0,-1], # Down, Up, Right, Left
                [1,-1],[1,1],[-1,-1],[-1,1] # Bottom left, bottom right, top left, top right
            ]

            nei = 0
            for (x, y) in directions:
                r, c = row + x, col + y

                if (
                    r in range(ROWS) and
                    c in range(COLS) and
                    board[r][c] in [1, 3] # 1 means originally a 1 and 3 means it was originally a 1
                ):
                    nei += 1

            return nei

        # Make changes to the state
        for row in range(ROWS):
            for col in range(COLS):
                nei = count_neighbors(row, col)

                if board[row][col] == 1: # Cell w/ 2 or 3 neighbors
                    if nei in [2, 3]:
                        board[row][col] = 3

                elif nei == 3: # Becomes a live cell
                    board[row][col] = 2

        # Update the board based on mapping
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                          board[row][col] = 1

# Time Complexity: O(8mn) because we are iterating through the whole matrix
# and checking all the neighbors.

# Space Complexity: O(1)

# Solution: https://www.youtube.com/watch?v=fei4bJQdBUQ