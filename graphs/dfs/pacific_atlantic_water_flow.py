class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        output = []

        def dfs(row, col, visited, prev_height):
            if (
                (row, col) in visited or
                row < 0 or col < 0 or
                row == ROWS or col == COLS or
                heights[row][col] < prev_height
            ):
                return

            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])

        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][col])

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pac and (row, col) in atl:
                    output.append([row, col])

        return output

# Time Complexity: O(N * M) bc ...?

# Space Complexity: O(N * M) bc we can at most have N * M values.

# Solution: https://www.youtube.com/watch?v=s-VkcjHqkGI