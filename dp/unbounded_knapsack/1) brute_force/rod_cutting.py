def solve_rod_cutting(lengths, prices, n):
  return helper(lengths, prices, n, 0)

def helper(lengths, prices, n, i):
  if i >= len(lengths) or n <= 0:
    return 0

  # recursive call after choosing the items at the currentIndex,
  # note that we recursive call on all items as we did not
  # increment currentIndex
  profit1 = 0
  if lengths[i] <= n:
    profit1 = prices[i] + helper(lengths, prices, n - lengths[i], i)

  # recursive call after excluding the element at the currentIndex
  profit2 = helper(lengths, prices, n, i + 1)

  return max(profit1, profit2)

def main():
  print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()