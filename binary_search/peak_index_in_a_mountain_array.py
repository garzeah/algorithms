class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        # We are using < because if we use <= we'll go out
        # of bounds since we're check the adj. pos. of mid
        while start < end:
            mid = (start + end) // 2

            # If the the middle is greater than both
            # start and end sides then we have found a peak
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            # Move it up since there's a bigger value on the right side
            elif arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1

        # Since we are using less than rather than <= both
        # start and end will finish at the same index
        return end

# Time Complexity: O(logN)
# Space Complexity: O(1)