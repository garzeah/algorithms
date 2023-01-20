class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.helper(cost, len(cost))

    def helper(self, cost, n):
        if n < len(cost):
            return 0

        if n == 0:
            return cost[0]

        if n == 1:
            return min(cost[0], cost[1])

        return min(
            cost[n - 1] + self.helper(cost, n - 1),
            cost[n - 2] + self.helper(cost, n - 2)
        )

# TC: O(2^n)
# SC: O(n)
