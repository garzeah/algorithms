def solve_knapsack(profits, weights, capacity):
  return helper(profits, weights, capacity, 0)

def helper(profits, weights, capacity, i):
  if i >= len(profits) or capacity <= 0:
    return 0

  # recursive call after choosing the items at the currentIndex,
  # note that we recursive call on all items as we did not
  # increment currentIndex
  profit1 = 0
  if weights[i] <= capacity:
    profit1 = profits[i] + helper(profits, weights, capacity - weights[i], i)

  # recursive call after excluding the element at the currentIndex
  profit2 = helper(profits, weights, capacity, i + 1)
  return max(profit1, profit2)

def main():
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()