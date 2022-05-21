def find_Kth_smallest_number(nums, k):
  max_heap = []

  for num in nums:
    if len(max_heap) < k:
      heappush(max_heap, -num)

    else:
      # Only pushing and popping if we have a smaller number
      if num < -max_heap[0]:
        heappushpop(max_heap, -num)

  return -max_heap[0]

# Time Complexity: O(n * log(k))
# Space Complexity: O(k)