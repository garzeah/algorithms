class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Want A to contain the smaller array
        if len(B) < len(A):
            A, B = B, A

        start, end = 0, len(A) - 1
        while True:
            i = (start + end) // 2 # A
            j = half - i - 2 # B, subtracting 2 to fix indexing issues

            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i + 1] if (i + 1) < len(A) else float('inf')
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j + 1] if (j + 1) < len(B) else float('inf')

            # Left partition of sorted numbers is correct
            if A_left <= B_right and B_left <= A_right:
                # Odd
                if (total % 2) > 0:
                    return min(A_right, B_right)

                # Even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right: # Reduce the size of the left partition for A
                end = i - 1
            else: # Increase the size of the left partition for A
                start = i + 1


# Time Complexity: Log(min(nums1, nums2)) since we're performing binary
# search on the smallest array.

# Space Complexity: O(m + n) for reassigning the arrays but can easily
# turn to O(1).

# Solution: https://www.youtube.com/watch?v=q6IEA26hvXc
