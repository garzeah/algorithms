class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                # If the value of the cell is 1, call the helper function
                if matrix[r][c] == 1:
                    res += self.helper(matrix, ROWS, COLS, r, c)

        return res

    def helper(self, matrix, ROWS, COLS, r, c):
        # If the indices are out of range or the value of the cell is 0, return 0
        if (
            r >= ROWS or
            c >= COLS or
            matrix[r][c] == 0
        ):
            return 0

        # If the value of the current cell is 1, the helper function is called
        # recursively for its right, bottom and bottom-right cells. We then
        # take the minimum of the returned values and add 1
        right = self.helper(matrix, ROWS, COLS, r, c + 1)
        bottom = self.helper(matrix, ROWS, COLS, r + 1, c)
        bottom_right = self.helper(matrix, ROWS, COLS, r + 1, c + 1)

        # Taking the minimum value ensures that we are only considering
        # square submatrices and 1 is added to count the cell itself as
        # it is also a 1×1 square submatrix
        return 1 + min(right, bottom, bottom_right)

# TC: O(m * n * 3^(mn))
# SC: O(m * n) bc of stack space