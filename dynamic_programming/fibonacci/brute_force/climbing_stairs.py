class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1

        if n < 0:
            return 0

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Time Complexity: O(N * 2^n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=Y0lT9Fck7qI