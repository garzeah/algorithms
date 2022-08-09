class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # A mapping of values we need to keep track of to simultaneously apply every rule
        # Original | State | Update
        #    0     |   0   |   0    # Nothing changes
        #    1     |   1   |   0    # Live cell dies when neighbors are < 2 or > 3
        #    1     |   2   |   1    # Live cell w/ 2 or 3 neighbors live on
        #    0     |   3   |   1    # Dead cell w/ 3 neighbors get to live

        ROWS, COLS = len(board), len(board[0])
        directions = [
            [1,0],[-1,0],[0,1],[0,-1],
            [1,1],[-1,-1],[-1,1],[1,-1]
        ]

        def count_neighbors(row, col):
            neis = 0

            for (x, y) in directions:
                r, c = row + x, col + y

                if (
                    r in range(ROWS) and
                    c in range(COLS) and
                    board[r][c] in [1, 2] # 1 means originally a 1 and 3 means it was originally a 1
                ):
                    neis += 1

            return neis

        # Make changes to the state
        for row in range(ROWS):
            for col in range(COLS):
                neis = count_neighbors(row, col)

                # Live cell
                if board[row][col] == 1:
                    if neis in [2, 3]: # Live cell w/ 2 or 3 neighbors live on
                        board[row][col] = 2

                # Dead cell
                elif board[row][col] == 0:
                    if neis == 3: # Dead cell w/ 3 neighbors gets to live
                        board[row][col] = 3

        # Update the board based on mapping
        for row in range(ROWS):
            for col in range(COLS):
                # A live cell that must be updated to a dead cell
                if board[row][col] == 1:
                    board[row][col] = 0

                # A live cell that must bed updated to a live cell
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1

# Time Complexity: O(8mn) because we are iterating through the whole matrix
# and checking all the neighbors.

# Space Complexity: O(1)

# Solution: https://www.youtube.com/watch?v=fei4bJQdBUQ