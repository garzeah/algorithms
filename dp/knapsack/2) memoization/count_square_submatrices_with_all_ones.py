class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0

        # Table to store the results of our subproblems
        memo = memo = [ [ -1 for x in range(COLS) ] for y in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                # If the value of the cell is 1, call the helper function
                if matrix[r][c] == 1 and memo[r][c] == -1:
                    res += self.helper(matrix, memo, ROWS, COLS, r, c)
                elif memo[r][c] != -1:
                    res += memo[r][c]

        return res

    def helper(self, matrix, memo, ROWS, COLS, r, c):
        # If the indices are out of range or the value of the cell is 0, return 0
        if (
            r >= ROWS or
            c >= COLS or
            matrix[r][c] == 0
        ):
            return 0

        if memo[r][c] != -1:
            return memo[r][c]

        # If the value of the current cell is 1, the helper function is called
        # recursively for its right, bottom and bottom-right cells. We then
        # take the minimum of the returned values and add 1
        right = self.helper(matrix, memo, ROWS, COLS, r, c + 1)
        bottom = self.helper(matrix, memo, ROWS, COLS, r + 1, c)
        bottom_right = self.helper(matrix, memo, ROWS, COLS, r + 1, c + 1)

        # Taking the minimum value ensures that we are only considering
        # square submatrices and 1 is added to count the cell itself as
        # it is also a 1×1 square submatrix
        memo[r][c] = 1 + min(right, bottom, bottom_right)
        return memo[r][c]

# TC: O(m * n)
# SC: O(m * n)