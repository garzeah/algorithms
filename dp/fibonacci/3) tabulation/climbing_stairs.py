class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [-1 for _ in range(n)]
        dp[0], dp[1] = 1, 2

        # Can use previous sub-solutions to arive at nth solution
        for i in range(2, n):
            two_step = dp[i - 2]
            one_step = dp[i - 1]
            dp[i] = one_step + two_step

        return dp[n - 1]

# Time Complexity: O(n)
# Space Complexity: O(n)