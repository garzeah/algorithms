class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Since it's n x n, we can get columns from
        # len(matrix) rather than len(matrix[0])
        left, right = 0, len(matrix) - 1

        while left < right:
            # Iterating through the entire row except last element
            for i in range(right - left):
                top, bottom = left, right

                # Save the top left value
                top_left = matrix[top][left + i]

                # Move the bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move top left into top right
                matrix[top + i][right] = top_left

            # Update our pointers
            left += 1
            right -= 1

        return matrix

# Time Complexity: O(n^2)
# Space Complexity: O(1)
