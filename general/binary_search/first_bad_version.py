# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        res = -1

        while l <= r:
            mid = (l + r) // 2

            # Keep moving down until we find it
            if isBadVersion(mid) == True:
                res = mid # Save previous var
                r = mid - 1
            # That means we can trim the left side since
            # all versions after a bad version are also bad
            else:
                l = mid + 1

        return res

# Time Solution: O(log(n))
# Time Complexity: O(1)