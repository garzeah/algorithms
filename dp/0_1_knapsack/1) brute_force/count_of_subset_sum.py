def count_subsets(num, target):
  return helper(num, target, 0)

def helper(num, target, i):
  if target == 0:
    return 1

  if target < 0 or i >= len(num):
    return 0

  # decision to include the number at the current index
  sum1 = 0
  if num[i] <= target:
    sum1 = helper(num, target - num[i], i + 1)

  # decision to not include the number at the current index
  sum2 = helper(num, target, i + 1)
  return sum1 + sum2


