class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        old_color = image[sr][sc]

        def dfs(row, col, i):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            image[row][col] = newColor

            for x, y in directions:
                r, c = row + x, col + y

                if (
                    r in range(ROWS) and
                    c in range(COLS) and
                    image[r][c] == old_color and
                    image[r][c] != newColor
                ):
                    dfs(r, c, i + 1)

        dfs(sr, sc, 0)
        return image

# Time Complexity: O(n * m)
# Space Complexity: O(n * m) bc of queue space.