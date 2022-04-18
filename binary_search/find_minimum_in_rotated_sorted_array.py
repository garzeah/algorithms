class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = float('inf')
        start, end = 0, len(nums) - 1

        while start <= end:
            # If we get to a subarray that is already sorted then
            # we can update our result to the min of itself
            if nums[start] < nums[end]:
                output = min(output, nums[start])
                break

            mid = (start + end) // 2
            output = min(output, nums[mid])

            # If it is part the of left sorted portion then
            # we want to search the right sorted portion
            if nums[mid] >= nums[start]:
                start = mid + 1
            # If it is part the of right sorted portion then
            # we want to search the left sorted portion
            else:
                end = mid - 1

        return output

# Time Complexity: O(logn)
# Space Complexity: O(1)