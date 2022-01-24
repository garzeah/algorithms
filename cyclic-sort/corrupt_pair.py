def find_corrupt_numbers(nums):
    i, n = 0, len(nums)

    while i < n:
        # Range is 1 to n, so we have dont have
        # to ignore n since we can place it in the array
        j = nums[i] - 1

        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        # Want the duplicate and want the missing number
        if nums[i] != i + 1:
            # Duplicate and missing number
            return [nums[i], i + 1]

# Time Complexity: O(n)
# Space Complexity: O(1)