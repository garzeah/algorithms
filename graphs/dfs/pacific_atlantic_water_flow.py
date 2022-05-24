class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visited, prev_height):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited.add((row, col))

            for x, y in directions:
                r, c = row + x, col + y

                if (
                    r in range(ROWS) and
                    c in range(COLS) and
                    (r, c) not in visited and
                    # If the current height is >= the the previous height
                    # then that means water can flow that ocean (pac or atl)
                    heights[r][c] >= prev_height
                ):
                    dfs(r, c, visited, heights[r][c])

        # For each border we know that whatever ocean it touches
        # that it can reach it. So we want to check for every
        # border whether or not the adjacent positions can
        # reach their respective ocean as well and whichever
        # overlaps is able to reach both.
        for col in range(COLS):
            dfs(0, col, pac, heights[0][col]) # Top
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col]) # Bottom

        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0]) # Left
            dfs(row, COLS - 1, atl, heights[row][COLS - 1]) # Right

        # Want to find out where the positions intersect since that
        # means that position can visit both the pacific and atlantic
        output = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pac and (row, col) in atl:
                    output.append([row, col])

        return output

# Time Complexity: O(N * M) where n and m is the rows and columns of
# the matrix. Also, we will be revisiting nodes at most a few times.

# Space Complexity: O(N * M) where n and m is the rows and columns of
# the matrix. We can only have at most n * m positions.

# Solution: https://www.youtube.com/watch?v=s-VkcjHqkGI