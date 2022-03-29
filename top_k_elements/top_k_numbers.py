def find_k_largest_numbers(nums, k):
  min_heap = []

  # Put first 'K' numbers in the min heap
  for i in range(k):
    heappush(min_heap, nums[i])

  # Go through the remaining numbers of the array, if the
  # number from the array is bigger than the top (smallest)
  # number of the min-heap, remove the top number from heap
  # and add the number from array.
  for i in range(k, len(nums)):
    if min_heap[0] < nums[i]:
        heappop(min_heap)
        heappush(min_heap, nums[i])

  # The heap has the top 'K' numbers
  return min_heap

# Time Complexity: O(n) * log(k)
# Space Complexity: O(k)