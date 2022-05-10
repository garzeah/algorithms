class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        # Want A to contain the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        start, end = 0, len(A) - 1

        while True:
            i = (start + end) // 2 # A
            j = half - i - 2 # B, subtracting 2 to fix indexing issues

            A_left = A[i] if i >= 0 else float('-inf')
            B_left = B[j] if j >= 0 else float('-inf')
            A_right = A[i + 1] if (i + 1) < len(A) else float('inf')
            B_right = B[j + 1] if (j + 1) < len(B) else float('inf')

            # Left partition of sorted numbers is correct
            if A_left <= B_right and B_left <= A_right:
                if (total % 2) == 0: # Even
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

                return min(A_right, B_right) # Odd
            # Reduce the size of the left partition for A
            # because we want all values of A to be less than B?
            elif A_left > B_right:
                end = i - 1
            # Increase the size of the left partition for A
            # because we want all values of A to be less than B?
            else:
                start = i + 1


# Time Complexity: Log(min(nums1, nums2)) since we're performing binary
# search on the smallest array.

# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=q6IEA26hvXc
