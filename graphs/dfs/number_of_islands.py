class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                # If we changed this to pop, it'd be iterative DFS
                row, col = queue.pop()
                # Right, left, up, down directions
                directions = [[1, 0], [-1, 0], [0, 1], [0, - 1]]

                # Checking for adjacent positions
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                            queue.append((r, c))
                            visited.add((r, c))

        # Doing bfs search whenever we find an island
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands

# Time Complexity: O((m x n)^2) worst case scenario because we
# traverse through each value once and when we're checking
# adjacent positions, we're checking values again.

# Space Complexity: O(m x n) worst case scenario our queue will
# have m x n elements because as we're visiting each value
# we add the row and column to the queue

# Solution: https://www.youtube.com/watch?v=pV2kpPD66nE
