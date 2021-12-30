def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target_sum:
            return [left, right]
        elif curr_sum > target_sum:
            right -= 1
        else:
            left += 1

# Time Complexity: O(n) b/c we make one pass
# Space Complexity: O(1) b/c we just initialize curr_sum, left, right