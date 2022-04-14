def find_Kth_smallest_number(nums, k):
    max_heap = []

    for i in range(len(nums)):
        heappush(max_heap, -nums[i])

        # We are continually removing the smallest values
        # in our min. heap until we have k values
        if len(max_heap) > k:
            heappop(max_heap)

    return -max_heap[0]

# Time Complexity: O(n * log(k))
# Space Complexity: O(k)