class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or target is None:
            return False

        for row in matrix:
            start, end = 0, len(row) - 1

            while start <= end:
                mid = (start + end) // 2

                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

        return False

# Time Complexity: m * log(n) where m is the amount of
# rows and n is the amount of columns.

# Space Complexity: O(1)