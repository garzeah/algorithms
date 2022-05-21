def find_k_largest_numbers(nums, k):
    min_heap = []

    for i in range(len(nums)):
        if len(min_heap) < k:
            heappush(min_heap, nums[i])
        else:
            # Only popping if we find a larger number
            if nums[i] > min_heap[0]:
                heappushpop(min_heap, nums[i])

    return min_heap[0]

# Time Complexity: O(n) * log(k)
# Space Complexity: O(k)