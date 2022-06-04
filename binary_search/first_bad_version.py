# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n + 1
        res = -1

        while start <= end:
            mid = (start + end) // 2

            if isBadVersion(mid) == True:
                res = mid
                end = mid - 1
            else:
                start = mid + 1

        return res

# Time Solution: O(log(n))
# Time Complexity: O(1)