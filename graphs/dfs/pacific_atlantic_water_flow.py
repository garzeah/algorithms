class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        output = []

        def dfs(row, col, visited, prev_height):
            if (
                (row, col) in visited or
                row < 0 or col < 0 or
                row == rows or col == cols or
                heights[row][col] < prev_height
            ):
                return

            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][col])

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl:
                    output.append([row, col])

        return output

# Time Complexity: O(N * M) bc ...?

# Space Complexity: O(N * M) bc we can at most have N * M values.

# Solution: https://www.youtube.com/watch?v=s-VkcjHqkGI