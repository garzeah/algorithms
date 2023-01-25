def count_subsets(num, target):
  memo = [ [ -1 for x in range(target + 1) ] for y in range(len(num)) ]
  return helper(num, memo, target, 0)

def helper(num, memo, target, i):
  if target == 0:
    return 1

  if target < 0 or i >= len(num):
    return 0

  if memo[i][target] != -1:
    return memo[i][target]

  # decision to include the number at the current index
  sum1 = 0
  if num[i] <= target:
    sum1 = helper(num, memo, target - num[i], i + 1)

  # decision to not include the number at the current index
  sum2 = helper(num, memo, target, i + 1)
  memo[i][target] = sum1 + sum2
  return memo[i][target]


