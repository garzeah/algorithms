class Solution:
    def climbStairs(self, n: int) -> int:
        # Base Case (Can reach top)
        if n == 0:
            return 1

        # Base Case (Can't reach top)
        if n < 0:
            return 0

        # Decision to take one and two steps
        one_step = self.climbStairs(n - 1)
        two_step = self.climbStairs(n - 2)

        return one_step + two_step

# Time Complexity: O(N * 2^n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=Y0lT9Fck7qI