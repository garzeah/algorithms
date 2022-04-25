class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1

        # We are using < because if we use <= we'll go out
        # of bounds for inputs with length that is less
        # than 3 since we're check the siblings of mid
        while start < end:
            mid = (start + end) // 2

            # If the the middle is greater than both
            # start and end sides then we have found a peak
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            # If mid is smaller than the next number, there must be a higher peak
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1
            # If mid is greater than the next number, then must be no higher peak
            else:
                end = mid - 1

        # Can return start or end since we are using
        # less than in a mountain array
        return end

# Time Complexity: O(logN)
# Space Complexity: O(1)
