class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.helper(coins, amount, 0)
        return -1 if res == float('inf') else res

    def helper(self, coins, amount, i):
        # Base case
        if amount == 0:
            return 0

        if amount < 0 or i >= len(coins):
            return float('inf')

        # recursive call after selecting the coin at the i
        # if the coin at i exceeds the amount, we shouldn't process this
        count1 = float('inf')
        if coins[i] <= amount:
            count1 = 1 + self.helper(coins, amount - coins[i], i)

    # recursive call after excluding the coin at the i
        count2 = self.helper(coins, amount, i + 1)

        return min(count1, count2)

# The time complexity of the above algorithm is exponential O(2^n), where ‘n’
# represents the total number. The space complexity is O(n), this memory
# which will be used to store the recursion stack.
