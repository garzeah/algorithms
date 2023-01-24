def can_partition(num):
  memo = [ [ -1 for x in range(sum(num) + 1) ] for y in range(len(num)) ]
  return helper(num, memo, 0, 0, 0)

def helper(num, memo, i, sum1, sum2):
  if i >= len(num):
    return abs(sum1 - sum2)

  if memo[i][sum1] != -1:
    return memo[i][sum1]

  # recursive call after including the number at the currentIndex in the first set
  diff1 = helper(num, memo, i + 1, sum1 + num[i], sum2)

  # recursive call after including the number at the currentIndex in the second set
  diff2 = helper(num, memo, i + 1, sum1, sum2 + num[i])
  memo[i][sum1] = min(diff1, diff2)

  return memo[i][sum1]

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()