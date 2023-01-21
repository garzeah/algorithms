class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one_step, two_step = cost[0], cost[1]

        # As we iterate through the array, we want to keep track of
        # the cheapest cost for one/two steps
        for i in range(2, len(cost)):
            temp = cost[i] + min(one_step, two_step)
            one_step = two_step
            two_step = temp

        return min(one_step, two_step)

# TC: O(n)
# SC: O(1)
# Solution: https://leetcode.com/problems/min-cost-climbing-stairs/discuss/476388/4-ways-or-Step-by-step-from-Recursion-greater-top-down-DP-greater-bottom-up-DP-greater-fine-tuning