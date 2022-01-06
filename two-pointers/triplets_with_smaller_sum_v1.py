def triplet_with_smaller_sum(arr, target):
  arr.sort()
  count = 0

  for i in range(len(arr)):
    left, right = i + 1, len(arr) - 1

    while left < right:
      curr_sum = arr[left] + arr[right]
      target_sum = target - arr[i]

      if curr_sum < target_sum:
        # Since arr[right] >= arr[left], therefore, we can replace
        # arr[right] by any number between left and right to get
        # a sum less than the target sum. The remaining counts
        # would be right - left
        count += right - left
        left += 1 # Need a bigger sum
      else:
        right -= 1 # Need a smaller sum

  return count

# Time Complexity: O(n^2)

# Space Complexity: The space complexity of the above algorithm
# will be O(N) which is required for sorting if we are not using
#  an in-place sorting algorithm.