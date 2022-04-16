class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        while start < end:
            mid = (start + end) // 2
            print(mid)
            # If the the middle is greater than both
            # start and end sides then we have found a peak
            if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                return mid

            # We don't have mid + 1 and mid - 1 because it is not
            # completely sorted and want to check if the values
            # next to it could possibly be a peak
            elif arr[mid] < arr[mid + 1]:
                start = mid
            else:
                end = mid

# Time Complexity: O(logN)
# Space Complexity: O(1)