class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        min_num = float('inf')

        while start <= end:
            while start < end and nums[start] == nums[start + 1]:
                start += 1
            while start < end and nums[end] == nums[end - 1]:
                end -= 1

            mid = (start + end) // 2
            min_num = min(min_num, nums[mid])

            # In the event we do not have a rotated sorted array,
            # anymore then we want to get the minimum value
            if nums[start] < nums[end]:
                min_num = min(min_num, nums[start])
                break
            # If it is part the of left sorted portion so
            # we want to search the right sorted portion
            elif nums[mid] >= nums[start]:
                start = mid + 1
            # If it is part the of right sorted portion do
            # we want to search the left sorted portion
            else:
                end = mid - 1

        return min_num

# Time Complexity: O(logn)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=nIVW4P8b1VA