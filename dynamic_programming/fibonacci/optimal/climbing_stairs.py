class Solution:
    def climbStairs(self, n: int) -> int:
        one_step, two_step = 1, 1

        # Since this follows the fibonacci sequence,
        # we can use the previous sub-problems to
        # arrive at the solution
        for _ in range(2, n + 1):
            temp = one_step
            one_step = one_step + two_step
            two_step = temp

        return one_step

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=Y0lT9Fck7qI