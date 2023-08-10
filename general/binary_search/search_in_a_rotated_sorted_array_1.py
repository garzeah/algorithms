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
                return mid

            # If in left sorted portion
            elif nums[mid] >= nums[start]:
                # If target is not between start and mid, search right side
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                # Otherwise, it is so search left side
                else:
                    end = mid - 1

            # If in right sorted portion
            else:
                # If target is not between mid and end, search left side
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                # Otherwise, it is so search right side
                else:
                    start = mid + 1

        return -1

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=U8XENwh8Oy8