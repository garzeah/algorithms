def find_Kth_smallest(lists, k):
    min_heap = []

    # Put the 1st element of each list in the min heap
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))

    # Take the smallest (top) element from the min heap,
    # if the running count is equal to k return the number
    num_count, num = 0, 0
    while min_heap:
        num, i, list = heappop(min_heap)
        num_count += 1
        if num_count == k:
            break
        # If the array of the top element has more
        # elements, add the next element to the heap
        if len(list) > i + 1:
            heappush(min_heap, (list[i+1], i+1, list))

    return num

# Time Complexity: Since we’ll be going through at most ‘K’
# elements among all the arrays, and we will remove/add one
# element in the heap in each step, the time complexity of
# the above algorithm will be O(K*logM) where ‘M’ is the
# total number of input arrays.

# Space Complexity: The space complexity will be O(M) because,
# at any time, our min-heap will be storing one number from all
# the ‘M’ input arrays.

