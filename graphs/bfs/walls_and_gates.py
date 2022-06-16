class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()

        # Want to find all the gates and perform
        # a multi-source BFS (where we do BFS)
        # at the same time
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0: # gate
                    queue.append((row, col))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        dist = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                rooms[row][col] = dist # Assigning the distance

                for x, y in directions:
                    r, c = row + x, col + y

                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visited and
                        rooms[r][c] != -1 and
                        rooms[r][c] != 0
                    ):
                        queue.append((r, c))
                        visited.add((r, c))
            dist += 1 # Updating the distance for every new set of directions we add

        return rooms

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Solution: https://www.youtube.com/watch?v=e69C6xhiSQE