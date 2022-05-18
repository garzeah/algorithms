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

        # Checking for cycles and if graph is connected
        return self.dfs(0, -1, visited, adj) and n == len(visited)

    def dfs(self, curr_node, prev, visited, adj):
        # If vertex is in visited, then we have a cycle
        if curr_node in visited:
            return False

        visited.add(curr_node)

        # Checking the neighbors of our vertex
        for nei in adj[curr_node]:
            # If our neighbor is equal to the previous vertex then we
            # want to continue since it is a false positive because
            # it'll be marked as visited marked as visited already
            if nei == prev:
                continue

            # Checking if the remaining vertices are are a valid tree
            if self.dfs(nei, curr_node, visited, adj) is False:
                return False

        return True

# Time Complexity: O(V + E) because we visit each node once.

# Space Complexity: O(V + E) because we make an adjaceny list of every node and edge.

# Solution: https://www.youtube.com/watch?v=bXsUuownnoQ

