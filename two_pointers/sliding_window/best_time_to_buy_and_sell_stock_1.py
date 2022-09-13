class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0

        for i in range(len(prices)):
            curr_price = prices[i]

            # Is it better to keep the current max or take the
            # curr_price - min_price?
            max_profit = max(max_profit, curr_price - min_price)

            # If we find a new min_price, update it in case we can
            # sell for more
            if curr_price < min_price:
                min_price = curr_price

        return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)