def rod_cutting(lengths, prices, n):
    memo = [ [ -1 for x in range(n + 1) ] for y in range(len(lengths)) ]
    return helper(lengths, prices, n, memo, 0)

def helper(lengths, prices, n, memo, i):
    if n <= 0 or i >= len(lengths):
        return 0

    if memo[i][n] != -1:
        return memo[i][n]

    profit1 = 0
    if lengths[i] <= n:
        profit1 = prices[i] + helper(lengths, prices, n - lengths[i], memo, i)

    profit2 = helper(lengths, prices, n, memo, i + 1)
    memo[i][n] = max(profit1, profit2)
    return memo[i][n]