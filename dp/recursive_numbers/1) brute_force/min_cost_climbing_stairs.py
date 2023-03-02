class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0, 0)
        return self.helper(cost, 0)

    def helper(self, cost, i):
        if i >= len(cost):
            return 0

        one_step = cost[i] + self.helper(cost, i + 1)
        two_step = cost[i] + self.helper(cost, i + 2)

        return min(one_step, two_step)