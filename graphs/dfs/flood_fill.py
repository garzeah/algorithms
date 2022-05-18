class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ROWS, COLS = len(image) - 1, len(image[0]) - 1

        def dfs(image, row, col, newColor, starting_pixel):
            if (
                row < 0 or row > ROWS or
                col < 0 or col > COLS or
                image[row][col] == newColor or
                image[row][col] != starting_pixel
            ):
                return

            image[row][col] = newColor
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for x, y in directions:
                r, c = row + x, col + y
                dfs(image, r, c, newColor, starting_pixel)

        dfs(image, sr, sc, newColor, image[sr][sc])
        return image

# Time Complexity: O(n * m)
# Space Complexity: O(n * m) bc of stack space.
# Solution: https://www.youtube.com/watch?v=hEZ8uGqaC2c
