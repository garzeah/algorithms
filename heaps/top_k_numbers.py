def find_k_largest_numbers(nums, k):
  min_heap = []

  for num in nums:
    if len(min_heap) < k:
      heappush(min_heap, num)
    else:
      # Only popping if we find a larger number
      if num > min_heap[0]:
        heappushpop(min_heap, num)

  return min_heap

# Time Complexity: O(n) * log(k)
# Space Complexity: O(k)