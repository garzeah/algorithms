def can_partition(num):
  return helper(num, 0, 0, 0)

def helper(num, i, sum1, sum2):
  if i >= len(num):
    return abs(sum1 - sum2)

  # recursive call after including the number at the currentIndex in the first set
  diff1 = helper(num, i + 1, sum1 + num[i], sum2)

  # recursive call after including the number at the currentIndex in the second set
  diff2 = helper(num, i + 1, sum1, sum2 + num[i])
  return min(diff1, diff2)

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()