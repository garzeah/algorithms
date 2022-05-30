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

            # If in left sorted portion, search right sorted portion
            elif nums[mid] >= nums[start]:
                # If mid is smaller than target or start is greater
                # than target, we want to search the right side
                if nums[mid] < target or nums[start] > target:
                    start = mid + 1
                # Otherwise, our mid is greater than target and our
                # start is less than target so search the left side
                else:
                    end = mid - 1

            # If in right sorted portion, search left sorted portion
            else:
                # If mid is bigger than target or end is smaller
                # than target, we want to search the left side
                if nums[mid] > target or nums[end] < target:
                    end = mid - 1
                # Otherwise, our mid is smaller than target and our
                # end is greater than target so search the right side
                else:
                    start = mid + 1

        return False

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=U8XENwh8Oy8