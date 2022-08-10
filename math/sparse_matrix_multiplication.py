class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ROWS_A, COLS_A = len(A), len(A[0])
        ROWS_B, COLS_B = len(B), len(B[0])

        # The size of the matrix will COLS_B * ROWS_A
        res = [[0 for x in range(COLS_B)] for y in range(ROWS_A)]

        for row in range(ROWS_A):
            for col in range(COLS_A):
                if A[row][col]: # If we encounter a non-zero number...
                    for k in range(COLS_B):
                        res[row][k] += A[row][col] * B[col][k]

        return res

# Time Complexity: O(ROWS_A * COLS_A * COLS_B)
# Space Complexity: O(ROWS_A * COLS_B)
# Solution: https://leetcode.com/problems/sparse-matrix-multiplication/discuss/76150/Java-and-Python-Solutions-with-and-without-Tables