def rod_cutting(lengths, prices, n):
    return helper(lengths, prices, n, 0)

def helper(lengths, prices, n, i):
    if n <= 0 or i >= len(lengths):
        return 0

    profit1 = 0
    if lengths[i] <= n:
        profit1 = prices[i] + helper(lengths, prices, n - lengths[i], i)

    profit2 = helper(lengths, prices, n, i + 1)
    return max(profit1, profit2)