class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k # Max start point

        while left < right:
            mid = (left + right) // 2

            # mid + k is closer to x, discard mid by assigning left = mid + 1
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1

            # mid is equal or closer to x than mid + k, remains mid as candidate
            else:
                right = mid

        # left == right, which makes both left and left + k have same diff with x
        return arr[left : left + k]

# Time Complexity: O(log(n - k) + k)
# Space Complexity: O(k)
# Solution: https://www.youtube.com/watch?v=o-YDQzHoaKM