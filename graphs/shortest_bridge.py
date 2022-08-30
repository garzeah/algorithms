class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        # Approach: We want to use DFS to mark one of the two islands
        # as an arbitrary number (e.g. 2). Once we do that, we want
        # to find every number that doesn't equal that arbitrary
        # number (e.g. 1). Then we will perform a multi-source
        # BFS search to calculate the distance it takes to
        # get to our arbitary number.

        # We want to use DFS or mark every island as a 2
        def dfs(row, col):
            if (
                row in range(ROWS) and
                col in range(COLS) and
                grid[row][col] == 1
            ):
                grid[row][col] = 2
                for (x, y) in directions:
                    r, c = row + x, col + y
                    dfs(r, c)

        # Using multi-source BFS to find the minimum distance of two islands
        queue, visited = deque(), set()
        def bfs(queue):
            while queue:
                row, col, dist = queue.popleft()

                if grid[row][col] == 2:
                    return dist

                for (x, y) in directions:
                    r, c = row + x, col + y

                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visited
                    ):
                        visited.add((r, c))
                        queue.append((r, c, dist + 1))

        # Creating a flag for whether we have found the first island or not
        is_first = False
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    if is_first is False:
                        is_first = True
                        dfs(row, col)
                    else:
                        queue.append((row, col, 0))

        # [0, 2]
        # [1, 0]
        # Performing our multi-source BFS search until we find
        # the minimum distance. We are subtracting 1 because
        # we account for the distance of finding 2 as well
        # which is something we don't want
        return bfs(queue) - 1

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Solution: https://leetcode.com/problems/shortest-bridge/discuss/1920292/DFS-%2B-BFS-SOLUTION-EXPLAIN-PROPELRY-EASY-TO-UNDERSTAND