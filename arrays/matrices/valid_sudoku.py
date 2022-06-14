class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # Contains all values per row
        cols = defaultdict(set) # Contains all values per col
        squares = defaultdict(set) # key = (r // 3, c // 3) # Contains all values per square

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if (
                    board[row][col] in rows[row] or # row contains a dupe
                    board[row][col] in cols[col] or # col contains a dupe
                    board[row][col] in squares[(row // 3, col // 3)] # square contains a dupe
                ):
                    return False

                # Record the values that occur in our rows, cols and squares
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])

        return True

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Solution: https://www.youtube.com/watch?v=TjFXEUCMqI8