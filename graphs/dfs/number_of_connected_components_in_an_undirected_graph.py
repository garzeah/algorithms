class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for vertex in range(n):
            adj[vertex] = []

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited, count = set(), 0
        # Using dfs to check each connected graph
        # then recording it in our adj_list
        for vertex in range(n):
            if vertex not in visited:
                self.dfs(adj, visited, vertex)
                count += 1

        return count

    def dfs(self, adj, visited, curr_node):
        if curr_node in visited:
            return

        # Recording each vertex we visit
        visited.add(curr_node)

        for nei in adj[curr_node]:
            self.dfs(adj, visited, nei)

# Time complexity: O(V + E) because we are traversing
# each node once.

# Space Complexity: O(V + E) to build out the adjaceny list.

# Solution: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/400707/Simple-DFS-and-BFS-Python-solutions-using-a-dictionary