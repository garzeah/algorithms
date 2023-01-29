import math


def count_ribbon_pieces(ribbonLengths, total):
  memo = [ [ -1 for x in range(total + 1) ] for y in range(len(ribbonLengths)) ]
  return helper(ribbonLengths, total, memo, 0)

def helper(ribbons, total, memo, i):
  if total == 0:
    return 0

  if i >= len(ribbons) or total < 0:
    return float('-inf')

  if memo[i][total] != -1:
    return memo[i][total]

  count1 = float('-inf')
  if ribbons[i] <= total:
    count1 = 1 + helper(ribbons, total - ribbons[i], memo, i)

  count2 = helper(ribbons, total, memo, i + 1)
  memo[i][total] = max(count1, count2)
  return memo[i][total]

def main():
  print(count_ribbon_pieces([2, 3, 5], 5))
  print(count_ribbon_pieces([2, 3], 7))
  print(count_ribbon_pieces([3, 5, 7], 13))
  print(count_ribbon_pieces([3, 5], 7))


main()