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

        # Checking for valid tree and if the graph is connected
        return self.dfs(adj, visited, 0, -1) and n == len(visited)

    def dfs(self, adj, visited, curr_node, prev):
        # If vertex is in visited, then we have a cycle
        if curr_node in visited:
            return False

        visited.add(curr_node)

        # Checking the neighbors of our vertex
        for nei in adj[curr_node]:
            # If our neighbor is equal to the previous vertex then we want to
            # continue since it is a false positive because it is marked as
            # visited already so we want to check the next neighbor
            if nei == prev:
                continue

            # Checking if have visited the remaining nodes, if
            # we have then we no lone have a valid tree anymore
            if self.dfs(adj, visited, nei, curr_node) is False:
                return False

        return True

# Time Complexity: O(V + E) because we visit each node once.

# Space Complexity: O(V + E) because we make an adjaceny list of every node and edge.

# Solution: https://www.youtube.com/watch?v=bXsUuownnoQ

