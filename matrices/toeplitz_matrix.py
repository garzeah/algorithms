class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(ROWS - 1):
            for col in range(COLS - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False

        return True

# Time Complexity: O(n * m)
# Space Complexity: O(1)