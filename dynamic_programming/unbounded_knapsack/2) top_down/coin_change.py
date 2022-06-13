class Solution:
    def coinChange(self, coins, amount):
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        result = self.helper(dp, coins, amount, 0)
        return -1 if result == float('inf') else result

    def helper(self, dp, coins, amount, idx):
        # base check
        if amount == 0:
            return 0

        if len(coins) == 0 or idx >= len(coins):
            return float('inf')

        # check if we have not already processed a similar sub-problem
        if dp[idx][amount] == -1:
            # recursive call after selecting the coin at the idx
            # if the coin at idx exceeds the amount, we shouldn't process this
            count1 = float('inf')
            res = float('inf')
            if coins[idx] <= amount:
                res = self.helper(dp, coins, amount - coins[idx], idx)
            if res != float('inf'):
                count1 = res + 1

            # recursive call after excluding the coin at the idx
            count2 = self.helper(dp, coins, amount, idx + 1)
            dp[idx][amount] = min(count1, count2)

        return dp[idx][amount]