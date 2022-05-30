class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        # Can use the previous sub-problems to
        # arrive at the solution
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)