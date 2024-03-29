class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = self.helper(coins, amount, 0)
        return res

    def helper(self, coins, target, i):
        if target == 0:
            return 1

        if i >= len(coins):
            return 0

        # recursive call after selecting the coin at the i
        # if the coin at i exceeds the amount, we shouldn't process this
        count1 = 0
        if coins[i] <= target:
            count1 += self.helper(coins, target - coins[i], i)

        # recursive call after excluding the coin at the i
        count2 = self.helper(coins, target, i + 1)

        return count1 + count2