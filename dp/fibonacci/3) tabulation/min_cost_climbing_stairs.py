class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n)]

        # As we iterate through the array, we want to keep track of
        # the cheapest cost for one/two steps
        for i in range(0, len(cost)):
            if i < 2: # Store the cost for one/two step
                dp[i] = cost[i]
            else: # For the current cost, find the cheapest b/twn one/two step
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])

# TC: O(n)
# SC: O(n)