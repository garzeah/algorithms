def solve_knapsack(profits, weights, capacity):
  return helper(profits, weights, capacity, 0)

def helper(profits, weights, capacity, idx):
  n = len(profits)
  # base checks
  if capacity <= 0 or n == 0 or len(weights) != n or idx >= n:
    return 0

  # recursive call after choosing the items at the idx, note that we recursive call on all
  # items as we did not increment idx
  profit1 = 0
  if weights[idx] <= capacity:
    profit1 = profits[idx] + helper(
      profits, weights, capacity - weights[idx], idx)

  # recursive call after excluding the element at the idx
  profit2 = helper(
    profits, weights, capacity, idx + 1)

  return max(profit1, profit2)