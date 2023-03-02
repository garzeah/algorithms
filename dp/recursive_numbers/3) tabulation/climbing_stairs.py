class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        cache = [-1 for _ in range(n)]
        cache[0], cache[1] = 1, 2

        # Can use previous sub-solutions to arive at nth solution
        for i in range(2, n):
            two_step = cache[i - 2]
            one_step = cache[i - 1]
            cache[i] = one_step + two_step

        return cache[n - 1]

# Time Complexity: O(n)
# Space Complexity: O(n)