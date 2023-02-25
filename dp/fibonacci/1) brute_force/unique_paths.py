class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [ [ 0 for y in range(n) ] for x in range(m) ]
        return self.helper(matrix, m, n, 0, 0)

    # Helper function to check the boundaries and base case
    def helper(self, matrix, m, n, x, y):

        # Out of bounds
        if (x == m or y == n):
            return 0

        # Check the base case when the last cell is reached
        if (x == m - 1 and y == n - 1):
            return 1

        # Using the recursive approach when moving right or down
        right = self.helper(matrix, m, n, x, y + 1)
        down = self.helper(matrix, m, n, x + 1, y)

        return right + down

# O(2^(n * m))
# O(n * m)