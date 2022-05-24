class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1

        # Since this follows the fibonacci sequence,
        # we can use the previous sub-problems to
        # arrive at the solution
        for i in range(2, n + 1):
            temp = n1
            n1 = n1 + n2
            n2 = temp

        return n1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=Y0lT9Fck7qI