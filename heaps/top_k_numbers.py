def find_k_largest_numbers(nums, k):
    min_heap = []

    for i in range(len(nums)):
        heappush(min_heap, nums[i])

        # We are continually removing the smallest values
        # in our min. heap until we have k values
        if len(min_heap) > k:
            heappop(min_heap)

    return min_heap

# Time Complexity: O(n) * log(k)
# Space Complexity: O(k)