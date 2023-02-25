class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [ [ -1 for x in range(n) ] for y in range(m) ]
        return self.helper(m, n, memo, 0, 0)

    # Helper function to check the boundaries and base case
    def helper(self, m, n, memo, x, y):

        # Out of bounds
        if (x == m or y == n):
            return 0

        # Check the base case when the last cell is reached
        if (x == m - 1 and y == n - 1):
            return 1

        if memo[x][y] != -1:
            return memo[x][y]

        # Using the recursive approach when moving right or down
        right = self.helper(m, n, memo, x, y + 1)
        down = self.helper(m, n, memo, x + 1, y)
        memo[x][y] = right + down

        return memo[x][y]

# O(n * m)
# O(n * m)