class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 0:
            return True

        adj, visited = {}, set()

        # Setting up our adjacent list
        for i in range(n):
            adj[i] = []

        # Adding our connections in our adjaceny list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Checking for cycles and if we have visited every node
        return self.dfs(0, -1, visited, adj) and n == len(visited)

    def dfs(self, vertex, prev, visited, adj):
        # If vertex is in visited, then we have a cycle
        if vertex in visited:
            return False

        visited.add(vertex)

        # Checking the neighbors of our vertex
        for nei in adj[vertex]:
            # If our neighbor is equal to the previous node
            # then skip to the next iteration because it is
            # a false positive since it is an undirected graph
            if nei == prev:
                continue

            # Checking if the remaining vertices are are a valid tree
            if self.dfs(nei, vertex, visited, adj) is False:
                return False

        return True

# Time Complexity: O(V + E) because we visit each node once.

# Space Complexity: O(V + E) because we make an adjaceny list of every node and edge.

# Solution: https://www.youtube.com/watch?v=bXsUuownnoQ

