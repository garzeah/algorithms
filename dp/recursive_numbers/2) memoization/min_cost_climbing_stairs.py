class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0, 0)
        memo = [ -1 for _ in range(len(cost)) ]
        return self.helper(cost, memo, 0)

    def helper(self, cost, memo, i):
        if i >= len(cost):
            return 0

        if memo[i] == - 1:
            one_step = cost[i] + self.helper(cost, memo, i + 1)
            two_step = cost[i] + self.helper(cost, memo, i + 2)
            memo[i] = min(one_step, two_step)

        return memo[i]