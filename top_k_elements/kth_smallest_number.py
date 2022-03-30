def find_Kth_smallest_number(nums, k):
    max_heap = []

    # Putting the first k numbers in the max heap
    for i in range(k):
        heappush(maxHeap, -nums[i])

    # Go through the remaining numbers of the array,
    # if the number from the array is smaller than the
    # top (biggest) number of the heap, remove the top
    # number from heap and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    # The root of the heap has the Kth smallest number
    return -max_heap[0]

# Time Complexity: O(n * log(k))
# Space Complexity: O(k)