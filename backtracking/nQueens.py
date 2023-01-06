class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # The queen can never share the same row, col, pos./neg. diag
        # otherwise they can attack each other
        cols = set() # keeps track of visited columns
        posDiag = set() # keeps track of pos. diags. (row + col), always constant
        negDiag = set() # keeps track of neg. diags. (row - col), always constant
        board, res = [["."] * n for i in range(n)], []

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                # Making sure queens cannot attack each other
                if (
                    col in cols or
                    (row + col) in posDiag or
                    (row - col) in negDiag
                ):
                    continue

                cols.add(col)
                posDiag.add((row + col))
                negDiag.add((row - col))
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                posDiag.remove((row + col))
                negDiag.remove((row - col))
                board[row][col] = "."

        backtrack(0)

        return res

# TC: 3^n
# SC: 3^n
# Solution: https://www.youtube.com/watch?v=Ph95IHmRp5M