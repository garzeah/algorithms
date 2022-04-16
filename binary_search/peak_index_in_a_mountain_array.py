class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            print(mid)
            # If the the middle is greater than both
            # left and right sides then we have found a peak
            if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                return mid

            # We don't have mid + 1 and mid - 1 because it is not
            # completely sorted and want to check if the values
            # next to it could possibly be a peak
            elif arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid

# Time Complexity: O(logN)
# Space Complexity: O(1)