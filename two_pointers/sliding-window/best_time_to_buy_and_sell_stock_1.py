class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        start = 0

        for end in range(len(prices)):
            curr_price = prices[end]
            # Recording the max profit in the current window
            max_profit = max(max_profit, curr_price - min_price)

            # Record the new minimum price and slide the
            # start of the window to the minimum
            if curr_price < min_price:
                min_price = curr_price
                start = end

        return max_profit

# Time Complexity: O(n)
# Space Complexity: O(1)