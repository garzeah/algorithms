class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visited, prev_height):
            visited.add((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

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

        # Using the top and bottom borders to check if a
        # position can visit the pacific and atlantic ocean
        for col in range(COLS):
            dfs(0, col, pac, heights[0][col]) # Top
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col]) # Bottom

        # Using the left and right borders to check if a
        # position can visit the pacific and atlantic ocean
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

# Time Complexity: O(N * M) bc ...?

# Space Complexity: O(N * M) bc we can at most have N * M values.

# Solution: https://www.youtube.com/watch?v=s-VkcjHqkGI