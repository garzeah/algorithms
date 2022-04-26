class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            # Shifting to remove duplicate elements
            while start < end and nums[start] == nums[start + 1]:
                start += 1
            while start < end and nums[end] == nums[end - 1]:
                end -= 1

            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            # If in left sorted portion
            elif nums[mid] >= nums[start]:
                # If target is greater than mid or smaller
                # than the start, search to the right
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                # Otherwise, search to the left
                else:
                    end = mid - 1

            # If in right sorted portion
            else:
                # If target is less than mid or greater than
                # the end, search to the left
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                # Otherwise, search to the right
                else:
                    start = mid + 1

        return False

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/1890363/python-or-binary-search-or-explained-or