class Solution:
    def coinChange(self, coins, amount):
        dp = [[-1 for x in range(amount + 1)] for y in range(len(coins))]
        result = self.helper(dp, coins, amount, 0)
        return -1 if result == float('inf') else result

    def helper(self, dp, coins, amount, i):
        # base check
        if amount == 0:
            return 0

        if len(coins) == 0 or i >= len(coins):
            return float('inf')

        # check if we have not already processed a similar sub-problem
        if dp[i][amount] == -1:
            # recursive call after selecting the coin at the i
            # if the coin at i exceeds the amount, we shouldn't process this
            count1 = float('inf')
            if coins[i] <= amount:
                res = self.helper(dp, coins, amount - coins[i], i)
                if res != float('inf'):
                    count1 = res + 1

            # recursive call after excluding the coin at the i
            count2 = self.helper(dp, coins, amount, i + 1)
            dp[i][amount] = min(count1, count2)

        return dp[i][amount]

# Since our memoization array dp[i][amount + 1] stores the results for all
# the subproblems, we can conclude that we will not have more than N*A
# subproblems (where ‘N’ is the number of items and ‘A’ is the amount
# capacity). This means that our time complexity will be O(N*A).

# The above algorithm will be using O(N*A) space for the memoization array.
# Other than that we will use O(N) space for the recursion call-stack. So
# the total space complexity will be O(N*A + N), which is asymptotically
# equivalent to O(N*A).
