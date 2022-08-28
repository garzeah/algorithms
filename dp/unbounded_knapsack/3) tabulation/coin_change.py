class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[float('inf') for _ in range(amount+1)] for _ in range(n)]

        # populate the amount=0 columns, as we don't need any coin to make zero amount
        for i in range(n):
            dp[i][0] = 0

        for i in range(n):
            for t in range(1, amount+1):
                if i > 0:
                    dp[i][t] = dp[i - 1][t]  # exclude the coin
                if t >= coins[i]:
                    if dp[i][t - coins[i]] != float('inf'):
                        # include the coin
                        dp[i][t] = min(dp[i][t], dp[i][t - coins[i]] + 1)

        # amount combinations will be at the bottom-right corner.
        return -1 if dp[n - 1][amount] == float('inf') else dp[n - 1][amount]
