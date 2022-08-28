class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Using a and b as points in both arrays and
        # using write to store the values in nums1
        a, b, write = m - 1, n - 1, m + n - 1

        # We are starting from the non-decreasing numbers
        # in A and B and will iterate through each value
        # and store them in corresponding order
        while b >= 0:
            if a >= 0 and A[a] > B[b]:
                A[write] = A[a]
                a -= 1
            else:
                A[write] = B[b]
                b -= 1

            write -= 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution: https://leetcode.com/problems/merge-sorted-array/discuss/1176400/Best-Python-Solution-Faster-Than-99-One-Loop-No-Splicing-No-Special-Case-Loop