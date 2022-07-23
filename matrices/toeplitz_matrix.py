class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row - 1][col - 1] != matrix[row][col]:
                    return False

        return True

# Time Complexity: O(n * m)
# Space Complexity: O(1)