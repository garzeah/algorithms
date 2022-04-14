def triplet_with_smaller_sum(arr, target):
  arr.sort()
  triplets = []

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
        for i in range(right, left, -1): # Adding a step of -1 bc of indexing
            triplets.append([arr[i], arr[left], arr[right]])
        left += 1 # Need a bigger sum
      else:
        right -= 1 # Need a smaller sum

  return triplets