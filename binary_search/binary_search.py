class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        is_ascending = nums[start] < nums[end]

        while start <= end:
            # Calculate the middle of the current range
            mid = start + (end - start) // 2

            if target == nums[mid]:
                return mid

            if is_ascending: # Ascending order
                if nums[mid] > target:
                    end = mid - 1  # The 'target' can be in the first half
                else:  # target > nums[mid]
                    start = mid + 1  # The 'target' can be in the second half
            else:  # Descending order
                if nums[mid] > target:
                    end = mid - 1  # The 'target' can be in the first half
                else:  # target < nums[mid]
                    start = mid + 1  # The 'target' can be in the second half

        return -1  # Element not found

# Time Complexity: Since, we are reducing the search range by half at every
# step, this means that the time complexity of our algorithm will be
# O(logN) where ‘N’ is the total elements in the given array.

# Space Complexity: The algorithm runs in constant space O(1).