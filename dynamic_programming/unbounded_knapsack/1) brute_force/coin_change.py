class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.helper(coins, amount, 0)
        return -1 if result == float('inf') else result


    def helper(self, coins, amount, start):
        # Base case
        if amount == 0:
            return 0

        n = len(coins)
        if n == 0 or start >= n:
            return float('inf')

        # recursive call after selecting the coin at the start
        # if the coin at start exceeds the amount, we shouldn't process this
        count1 = float('inf')
        if coins[start] <= amount:
            res = self.helper(coins, amount - coins[start], start)
            if res != float('inf'):
                count1 = res + 1

        # recursive call after excluding the coin at the start
        count2 = self.helper(coins, amount, start + 1)

        return min(count1, count2)