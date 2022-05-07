class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited = set()
        count = 0

        # Using dfs to check each connected graph
        # then recording it in our adj_list
        for vertex in range(n):
            if vertex not in visited:
                self.dfs(vertex, edges, visited, adj_list)
                count += 1

        return count

    def dfs(self, vertex, edges, visited, adj_list):
        if vertex in visited:
            return

        # Recording each vertex we visit
        visited.add(vertex)

        for node in adj_list[vertex]:
            self.dfs(node, edges, visited, adj_list)

# Time complexity: O(V + E) because we are traversing
# each node once.

# Space Complexity: O(V + E) to build out the adjaceny list.