class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, columns = set(), set()

        # For every value that equals zero, we want to record
        # which row and column we will set to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i);
                    columns.add(j);

        # Setting entire row to 0
        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0;

        # Setting entire column to 0
        for col in columns:
            for i in range(len(matrix)):
                matrix[i][col] = 0;

# Time Complexity: O(n*m)
# Space Complexity: O(n+m)
