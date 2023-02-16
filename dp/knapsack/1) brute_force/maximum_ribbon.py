def count_ribbon_pieces(n, sizes):
  return helper(n, sizes, 0)

def helper(n, sizes, i):
  if n == 0:
    return 0

  if n < 0 or i >= len(sizes):
    return float('-inf')

  count1 = float('-inf')
  if sizes[i] <= n:
    max_size = helper(n - sizes[i], sizes, i)
    if max_size != -1:
      count1 = 1 + max_size

  count2 = helper(n, sizes, i + 1)
  return max(count1, count2)