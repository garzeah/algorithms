class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0 for _ in range(n + 1)]
        return self.helper(n, cache)

    def helper(self, n, cache):
        # Base Case (Can reach top)
        if n == 0:
            return 1

        # Base Case (Can't reach top)
        if n < 0:
            return 0

        # If the call hasn't been made before, then it is time to record it
        if cache[n] == 0:
            one_step = self.helper(n - 1, cache)
            two_step = self.helper(n - 2, cache)
            cache[n] = one_step + two_step

        return cache[n]


# Time Complexity: O(N) because since we are using memoization, we are
# not having to do repeated calls anymore.

# Space Complexity: O(N) to store the space of the recursion stack
# where N is the length of the array.

# Solution: https://www.youtube.com/watch?v=Y0lT9Fck7qI