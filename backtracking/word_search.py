class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue, visited = deque(), set()
        max_area = 0

        def dfs(row, col):
            local_area = 1
            visited.add((row, col))

            for (x, y) in [[1,0],[-1,0],[0,1],[0,-1]]:
                r, c = row + x, col + y

                if (
                    r in range(ROWS) and
                    c in range(COLS) and
                    (r, c) not in visited and
                    grid[r][c] == 1
                ):
                    local_area += dfs(r, c)

            return local_area



        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, dfs(row, col))

        return max_area
