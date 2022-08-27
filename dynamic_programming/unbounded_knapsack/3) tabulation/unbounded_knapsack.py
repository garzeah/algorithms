def solve_knapsack(profits, weights, capacity):
  n = len(profits)
  # base checks
  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

  # populate the capacity=0 columns
  for i in range(n):
    dp[i][0] = 0

  # process all sub-arrays for all capacities
  for i in range(n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      if weights[i] <= c:
        profit1 = profits[i] + dp[i][c - weights[i]]
      if i > 0:
        profit2 = dp[i - 1][c]
      dp[i][c] = profit1 if profit1 > profit2 else profit2

  # maximum profit will be in the bottom-right corner.
  return dp[n - 1][capacity]