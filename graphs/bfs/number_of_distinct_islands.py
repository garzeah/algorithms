class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        visited = set()
        shapes = set() # Keeps track of all shapes once they've been normalized (turned into the origin)

        def bfs(row, col):
            rootRow, rootCol = row, col
            queue = deque([(row, col)])
            shape = []

            while queue:
                row, col = queue.popleft()

                for x, y in directions:
                    r, c = row + x, col + y

                    # We can find the origin of a point by subtracting the current directions
                    # with the rootRow and rootCol (points used upon starting BFS)
                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visited and
                        grid[r][c] == 1
                    ):
                        queue.append((r, c))
                    visited.add((r, c))
                        shape.append((r - rootRow, c - rootCol))

            shapes.add(tuple(shape)) # Turning into a tuple for O(1) lookup


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    bfs(row, col)

        return len(shapes)

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Solution: https://leetcode.com/problems/number-of-distinct-islands/discuss/108511/Simple-Python-Code-using-BFS-and-HashSet-with-Explanation/469710