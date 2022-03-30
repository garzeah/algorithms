def find_k_largest_numbers(nums, k):
  min_heap = []

  for i in range(len(nums)):
    # Go through the remaining numbers of the array, if the
    # number from the array is bigger than the top (smallest)
    # number of the min-heap, remove the top number from heap
    # and add the number from array.
    if i >= k - 1 and nums[i] > min_heap[0]:
      heappop(min_heap)
      heappush(min_heap, nums[i])
    else: # Putting first 'K' numbers in the min heap
      heappush(min_heap, nums[i])

  return min_heap

# Time Complexity: O(n) * log(k)
# Space Complexity: O(k)