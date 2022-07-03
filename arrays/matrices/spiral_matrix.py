class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0]) # Bc of the range of left to right (right is exclusive)
        output = []

        while left < right and top < bottom:
            # Get every i in the top row
            for i in range(left, right):
                output.append(matrix[top][i])

            top += 1 # Shifting top down by 1

            # Get every i in the right column
            for i in range(top, bottom):
                output.append(matrix[i][right - 1]) # -1 bc right is out of bounds

            right -= 1 # Shifting it to the left by 1

            # If the pointers have crossed then break
            # otherwise we will get repeating values
            if left >= right or top >= bottom:
                break

            # Get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[bottom - 1][i])

            bottom -= 1 # Shifting it upwards

            # Get every i in the left column
            for i in range(bottom - 1, top - 1, -1):
                output.append(matrix[i][left])

            left += 1 # Shifting it to the right by 1

        return output


# Time Complexity: O(n*m)
# Space Complexity: O(n*m)
# Solution: https://www.youtube.com/watch?v=BJnMZNwUk1M