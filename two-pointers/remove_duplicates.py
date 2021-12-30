def remove_duplicates(arr):
  left, right = 0, 1

  while right < len(arr):
    if arr[left] != arr[right]:
      left += 1
      arr[left] = arr[right]

    right += 1

  return left + 1

# Time Complexity: O(n) bc we make one pass
# Space Complexity: O(1)