def shortest_window_sort(arr):
    left, right = 0, len(nums) - 1

    # Find the first number out of sorting order from the beginning
    while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
        left += 1

    if left == len(nums) - 1: # Array is sorted
        return 0

    # Find the first number out of sorting order from the end
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    # Find the max and min of the subarray
    subarray_max = float('-inf')
    subarray_min = float('inf')
    for i in range(left, right + 1):
        subarray_max = max(subarray_max, nums[i])
        subarray_min = min(subarray_min, nums[i])

    # Extend the subarray to include any number which is
    # bigger than the minimum of the subarray
    while left > 0 and nums[left - 1] > subarray_min:
        left -= 1

    # Extend the subarray to include any number which is
    # smaller than the maximum of the subarray
    while right < len(nums) - 1 and nums[right + 1] < subarray_max:
        right += 1

    return right - left + 1

  # Time Complexity: O(n)
  # Space Complexity: O(1)