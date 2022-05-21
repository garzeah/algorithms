class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []

        # Building out our adjaceny list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        count = 0

        # For each vertex, we want to calculate the number of
        # times we do one cycle of bfs per connected graph
        for vertex in range(n):
            if vertex in visited:
                continue

            queue = deque([vertex])

            while queue:
                vertex = queue.popleft()

                if vertex in visited:
                    continue

                visited.add(vertex)

                for nei in adj[vertex]:
                    queue.append(nei)

            count += 1

        return count

# Time complexity: O(V + E) because we are traversing
# each node once.

# Space Complexity: O(V + E) to build out the adjaceny list.

# Solution: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/400707/Simple-DFS-and-BFS-Python-solutions-using-a-dictionary