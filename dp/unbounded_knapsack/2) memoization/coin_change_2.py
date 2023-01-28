class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for x in range(amount + 1)] for y in range(len(coins))]
        res = self.helper(coins, amount, dp, 0)
        return res

    def helper(self, coins, target, dp, i):
        if target == 0:
            return 1

        if i >= len(coins):
            return 0

        # recursive call after selecting the coin at the i
        # if the coin at i exceeds the amount, we shouldn't process this
        if dp[i][target] == -1:
            count1 = 0
            if coins[i] <= target:
                count1 += self.helper(coins, target - coins[i], dp, i)

            # recursive call after excluding the coin at the i
            count2 = self.helper(coins, target, dp, i + 1)
            dp[i][target] = count1 + count2

        return dp[i][target]