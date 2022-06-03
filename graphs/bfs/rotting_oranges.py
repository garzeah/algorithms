class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time, fresh = 0, 0

        # Want to get the total count of fresh oranges
        # and append rotten tomatoes to our queue
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append([row, col])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            # Want to search all starting rotten tomatoes simultaneously
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for x, y in directions:
                    r, c = row + x, col + y

                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1 # Fresh
                    ):
                        fresh -= 1 # Decrement fresh
                        grid[r][c] = 2 # Make rotten
                        queue.append([r, c]) # Check adj. positions
            time += 1

        # If there is still a remaining fresh orange, return -1
        return time if fresh == 0 else -1

# Time Complexity: O(n * m)
# Space Compelxity: O(n * m)
# Solution: https://www.youtube.com/watch?v=y704fEOx0s0