class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        # Since this follows the fibonacci sequence,
        # we can use the previous sub-problems to
        # arrive at the solution
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=Y0lT9Fck7qI