# Maximum Sum Subarray of Size K
def max_sub_array_of_size_k(k, arr):
  max_sum, window_sum = float('-inf'), 0
  start = 0

  for end in range(len(arr)):
    window_sum += arr[end] # add the next element

    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if end >= k - 1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[start] # subtract the element going out
      start += 1 # slide the window ahead

  return max_sum

# Time Complexity: 