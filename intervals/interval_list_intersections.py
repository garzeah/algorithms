class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        result = []
        i, j, start, end = 0, 0, 0, 1

        while i < len(a) and j < len(b):
            # Check if intervals overlap and a[i]'s start time lies within b[j]
            a_overlaps_b = a[i][start] >= b[j][start] and a[i][start] <= b[j][end]

            # Check if intervals overlap and b[j]'s start time lies within a[i]
            b_overlaps_a = b[j][start] >= a[i][start] and b[j][start] <= a[i][end]

            # Store the the intersection part
            if (a_overlaps_b or b_overlaps_a):
                result.append([max(a[i][start], b[j][start]), min(a[i][end], b[j][end])])

            # Move the interval that finishes first
            if a[i][end] < b[j][end]:
                i += 1
            else:
                j += 1

        return result

# Time Complexity: O(N + M), where 'N' and 'M' are the total
# number of intervals in the input arrays

# Space Comeplexity: O(N)