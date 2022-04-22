class Solution(object):
    def searchRange(self, nums, target):
        start, end = 0, len(nums) - 1

        first = self.findFirstIndex(nums, start, end, target)
        last = self.findLastIndex(nums, start, end, target)

        return [first, last]

    def findFirstIndex(self, nums, start, end, target):
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                res = mid
                end = mid - 1 # Left bias, will keep shifting right until start index of target
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return res

    def findLastIndex(self, nums, start, end, target):
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                res = mid
                start = mid + 1 # Right bias, will keep shifting left until last index of target
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return res

# Time Complexity: O(log(n))
# Space Complexity: O(1)