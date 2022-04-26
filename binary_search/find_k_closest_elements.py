class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, len(arr) - k # Max start point

        while start < end:
            mid = (start + end) // 2

            # mid + k is closer to x, discard mid by assigning start = mid + 1
            if x - arr[mid] > arr[mid + k] - x:
                start = mid + 1

            # mid is equal or closer to x than mid + k, remains mid as candidate
            else:
                end = mid

        # start == end, which makes both start and start + k have same diff with x
        return arr[start : start + k]

# Time Complexity: O(log(n - k) + k)
# Space Complexity: O(k)
# Solution: https://www.youtube.com/watch?v=o-YDQzHoaKM