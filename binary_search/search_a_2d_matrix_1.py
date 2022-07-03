class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or target is None:
            return False

        start, end = 0, len(matrix) * len(matrix[0]) - 1

        while start <= end:
            mid = (start + end) // 2 # Finds middle-most value in the matrix

            # We can find the row position by doing mid // column length
            i = mid // len(matrix[0])

            # We can find the column position by doing mid % column length
            j = mid % len(matrix[0])

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False

# Time Complexity: O(log(m * n)) where m and n are rows and cols.
# Space Complexity: O(1)
# Solution: https://www.youtube.com/watch?v=FOa55B9Ikfg