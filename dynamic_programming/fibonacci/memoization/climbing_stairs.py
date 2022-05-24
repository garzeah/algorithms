class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for x in range(n + 1)]
        return self.climb_stairs_recursive(dp, n)

    def climb_stairs_recursive(self, dp, n):
        # Base Case (Can reach top)
        if n == 0:
            return 1

        # Base Case (Can't reach top)
        if n < 0:
            return 0

        # If the call hasn't been made before, then it is time to record it
        if dp[n] == 0:
            one_step = self.climb_stairs_recursive(dp, n - 1)
            two_step = self.climb_stairs_recursive(dp, n - 2)
            dp[n] = one_step + two_step

        return dp[n]


# Time Complexity: O(N) because since we are using memoization, we are
# not having to do repeated calls anymore.

# Space Complexity: O(N) to store the space of the recursion stack
# where N is the length of the array.

# Solution: https://www.youtube.com/watch?v=Y0lT9Fck7qI