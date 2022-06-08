def solve_knapsack(profits, weights, capacity):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
  return helper(dp, profits, weights, capacity, 0)


def helper(dp, profits, weights, capacity, idx):

  # base checks
  if capacity <= 0 or idx >= len(profits):
    return 0

  # if we have already solved a similar problem, return the result from memory
  if dp[idx][capacity] != -1:
    return dp[idx][capacity]

  # recursive call after choosing the element at the idx
  # if the weight of the element at idx exceeds the capacity, we
  # shouldn't process this
  profit1 = 0
  if weights[idx] <= capacity:
    profit1 = profits[idx] + helper(
      dp, profits, weights, capacity - weights[idx], idx + 1)

  # recursive call after excluding the element at the idx
  profit2 = helper(
    dp, profits, weights, capacity, idx + 1)

  dp[idx][capacity] = max(profit1, profit2)
  return dp[idx][capacity]