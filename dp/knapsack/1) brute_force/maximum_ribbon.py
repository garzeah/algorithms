import math


def count_ribbon_pieces(ribbonLengths, total):
  return helper(ribbonLengths, total, 0)

def helper(ribbons, total, i):
  if total == 0:
    return 0

  if i >= len(ribbons) or total < 0:
    return float('-inf')

  count1 = float('-inf')
  if ribbons[i] <= total:
    count1 = 1 + helper(ribbons, total - ribbons[i], i)

  count2 = helper(ribbons, total, i + 1)
  return max(count1, count2)

def main():
  print(count_ribbon_pieces([2, 3, 5], 5))
  print(count_ribbon_pieces([2, 3], 7))
  print(count_ribbon_pieces([3, 5, 7], 13))
  print(count_ribbon_pieces([3, 5], 7))


main()