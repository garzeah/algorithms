class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, columns = [], []

        # For every value that equals zero, we want to record
        # which row and column we will set to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i);
                    columns.append(j);

        # Setting entire row to 0
        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0;

        # Setting entire column to 0
        for col in columns:
            for i in range(len(matrix)):
                matrix[i][col] = 0;

# Time Complexity: O(n*m) where n is the length of columns and m is
# the length of the rows.

# Space Complexity: O(n+m) where m is the length of the rows set and
# n is the length of the columns set.
