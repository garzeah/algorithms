class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Setting up our adjacent list
        adj = {}
        for vertex in range(n):
            adj[vertex] = []

        # Adding our connections in our adjaceny list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        # A valid tree means that...
        #   - And there are no loops
        #   - All nodes are connected
        return self.dfs(adj, visited, -1, 0) and n == len(visited)

    def dfs(self, adj, visited, prev, curr):
        # If vertex is in visited, then we have a cycle
        if curr in visited:
            return False

        visited.add(curr)

        # Checking the neighbors of our vertex
        for nei in adj[curr]:
            # If our neighbor is equal to the previous vertex then we want to
            # continue since it is a false positive because it is marked as
            # visited already so we want to check the next neighbor
            if nei == prev:
                continue

            # If we find a node that has already been visited, it
            # has a cycle so we have to return False
            if self.dfs(adj, visited, curr, nei) is False:
                return False

        return True

# Time Complexity: O(V + E) because we visit each node once.

# Space Complexity: O(V + E) because we make an adjaceny list of every node and edge.

# Solution: https://www.youtube.com/watch?v=bXsUuownnoQ

