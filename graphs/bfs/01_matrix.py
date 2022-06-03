class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                # Find all the 0s and append to our queue
                # since we will use those for searching
                if mat[row][col] == 0:
                    queue.append((row, col))
                # Set to "T" so when we find it when doing BFS we can add
                # the previous position with 1 iteratively. Otherwise, if
                # we did nothing and searched for 1 instead all the
                # adjacent 0's would add one to it
                else:
                    mat[row][col] = "T"

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue:
            row, col = queue.popleft()

            for x, y in directions:
                r, c = row + x, col + y

                if (
                    r in range(ROWS) and
                    c in range(COLS) and
                    mat[r][c] == "T"
                ):
                    # Adds the previous everytime we find a "T"
                    mat[r][c] = mat[row][col] + 1
                    queue.append((r, c))

        return mat

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Solution: https://www.youtube.com/watch?v=hIvMZFqjs_A