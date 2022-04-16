class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Since it's n x n, we can get columns from
        # len(matrix) rather than len(matrix[0])
        left, right = 0, len(matrix[0]) - 1

        while left < right:
            # Iterating through the entire row except last element
            for i in range(right - left):
                top, bottom = left, right

                # Save the top left value
                top_left = matrix[top][left + i]

                # Replace top left with bottom left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Replace bottom left with bottom right
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Replace bottom right with top right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Replace top right with top left
                matrix[top + i][right] = top_left

            # Update our pointers
            left += 1
            right -= 1

        return matrix

# Time Complexity: O(n^2) since we are looking at each cell only once.

# Space Complexity: O(1)

# Solution: https://www.youtube.com/watch?v=fMSJSS7eO1w
