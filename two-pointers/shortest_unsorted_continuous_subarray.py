def shortest_window_sort(arr):
  low, high = 0, len(arr) - 1
  # Find the first number out of sorting order from the beginning
  while (low < len(arr) - 1 and arr[low] <= arr[low + 1]):
    low += 1

  if low == len(arr) - 1:  # If the array is sorted
    return 0

  # Find the first number out of sorting order from the end
  while (high > 0 and arr[high] >= arr[high - 1]):
    high -= 1

  # Find the maximum and minimum of the subarray
  subarray_max = -math.inf
  subarray_min = math.inf
  for k in range(low, high + 1):
    subarray_max = max(subarray_max, arr[k])
    subarray_min = min(subarray_min, arr[k])

  # To sort the whole array we need to include all such elements that are smaller than the
  # biggest element of the subarray.
  # Extend the subarray to include any number which is bigger than the minimum of the subarray
  while (low > 0 and arr[low - 1] > subarray_min):
    low -= 1
  # Extend the subarray to include any number which is smaller than the maximum of the subarray
  while (high < len(arr) - 1 and arr[high + 1] < subarray_max):
    high += 1

  return high - low + 1

  # Time Complexity: O(n)
  # Space Complexity: O(1)