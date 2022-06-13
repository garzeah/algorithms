class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.helper(coins, amount, 0)
        return -1 if result == float('inf') else result

    def helper(self, coins, amount, idx):
        # Base case
        if amount == 0:
            return 0

        if len(coins) == 0 or idx >= len(coins):
            return float('inf')

        # recursive call after selecting the coin at the idx
        # if the coin at idx exceeds the amount, we shouldn't process this
        count1 = float('inf')
        if coins[idx] <= amount:
            res = self.helper(coins, amount - coins[idx], idx)
            if res != float('inf'):
                count1 = res + 1

        # recursive call after excluding the coin at the idx
        count2 = self.helper(coins, amount, idx + 1)

        return min(count1, count2)