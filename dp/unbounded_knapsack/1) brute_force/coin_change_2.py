class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = self.helper(coins, amount, 0)
        return res

    def helper(self, coins, target, i):
        if target == 0:
            return 1

        if i >= len(coins):
            return 0

        count1 = 0
        if coins[i] <= target:
            count1 += self.helper(coins, target - coins[i], i)

        count2 = self.helper(coins, target, i + 1)

        return count1 + count2