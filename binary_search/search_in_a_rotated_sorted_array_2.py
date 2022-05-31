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

            # If in left sorted portion...
            elif nums[mid] >= nums[start]:
                # If target is within the range of the left sorted portion, search it
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                # Else target is not within range of the left
                # sorted portion search to the right of it
                else:
                    start = mid + 1

            # If in right sorted portion...
            else:
                # If target is within the range of the right sorted portion, search it
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                # Else target is not within range of the right
                # sorted portion so search to the left of it
                else:
                    end = mid - 1

        return False

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=U8XENwh8Oy8