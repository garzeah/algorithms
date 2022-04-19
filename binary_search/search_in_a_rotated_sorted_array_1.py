class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # Left sorted portion
            elif nums[mid] >= nums[start]:
                if nums[mid] < target or nums[start] > target:
                    start = mid + 1
                else:
                    end = mid - 1

            # Right sorted portion
            else:
                if nums[mid] > target or nums[end] < target:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=U8XENwh8Oy8