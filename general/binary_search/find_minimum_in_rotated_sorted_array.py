class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        min_num = float('inf')

        while start <= end:
            # If we get to a subarray that is already sorted then
            # we can update our result to the min of itself
            # and break out of the loop
            if nums[start] < nums[end]:
                min_num = min(min_num, nums[start])
                break

            mid = (start + end) // 2
            min_num = min(min_num, nums[mid])

            # If it is part the of left sorted portion so
            # we want to search the right sorted portion
            if nums[mid] >= nums[start]:
                start = mid + 1
            # If it is part the of right sorted portion do
            # we want to search the left sorted portion
            else:
                end = mid - 1

        return min_num

# Time Complexity: O(logn)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=nIVW4P8b1VA