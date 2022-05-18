class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        directions = [[1, 0], [-1, 0],[0, 1], [0, -1]] # All possible directions
        starting_pixel = image[sr][sc] # The current color of our pixel
        queue = deque([[sr,sc]]) # Initialise the queue for BFS

        while queue:
            row, col = queue.popleft()
            image[row][col] = newColor # Update the colour with newColor

            for x, y in directions:
                r, c = row + x, col + y
                if (
                    r in range(ROWS) and
                    c in range(COLS) and
                    image[r][c] != newColor and
                    image[r][c] == starting_pixel
                ):
                    queue.append((r, c))

        return image

# Time Complexity: O(n * m)
# Space Complexity: O(n * m) bc of queue space.