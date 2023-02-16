import math

def count_ribbon_pieces(n, sizes):
  memo = [ [ -1 for x in range(n + 1) ] for y in range(len(sizes)) ]
  return helper(n, sizes, memo, 0)

def helper(n, sizes, memo, i):
  if n == 0:
    return 0

  if n < 0 or i >= len(sizes):
    return -1

  if memo[i][n] != -1:
    return memo[i][n]

  count1 = -1
  if sizes[i] <= n:
    max_size = helper(n - sizes[i], sizes, memo, i)
    if max_size != -1:
      count1 = 1 + max_size

  count2 = helper(n, sizes, memo, i + 1)
  memo[i][n] = max(count1, count2)
  return memo[i][n]
