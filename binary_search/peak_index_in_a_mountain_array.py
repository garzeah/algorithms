class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        # We are using < because if we use <= we'll go out
        # of bounds since we're check the siblings of mid
        while start < end:
            mid = (start + end) // 2

            # If the the middle is greater than both
            # start and end sides then we have found a peak
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1

        # Can return start or end since we are using
        # less than in a mountain array
        return end

# Time Complexity: O(logN)
# Space Complexity: O(1)