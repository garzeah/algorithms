class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1

        while start < end:
            mid = (start + end) // 2

            # If the the middle is greater than both
            # start and end sides then we have found a peak
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid

            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1

        # If the length of the input is 1 then return either
        # start or end, if not then it is of size 2 so return end
        return end if arr[start] == arr[end] else end

# Time Complexity: O(logN)
# Space Complexity: O(1)
