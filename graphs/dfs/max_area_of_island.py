class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            local_max = 1

            while queue:
                row, col = queue.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for x, y in directions:
                    r, c = row + x, col + y
                    if (
                        (r, c) not in visited and
                        r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1
                    ):
                        queue.append((r, c))
                        visited.add((r, c))
                        local_max += 1

            return local_max


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    local_max = bfs(row, col)
                    max_area = max(max_area, local_max)


        return max_area

# Time Complexity: O((m x n)^2) worst case scenario because we
# traverse through each value once and when we're checking
# adjacent positions, we're checking values again.

# Space Complexity: O(m x n) worst case scenario our queue will
# have m x n elements because as we're visiting each value
# we add the row and column to the queue