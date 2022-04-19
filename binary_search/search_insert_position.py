class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        # Whenever binary search finishes, our start
        # will be in the position it would've been
        # if it were inside the array
        return start

# Time Complexity: O(logN)
# Space Complexity: O(1)