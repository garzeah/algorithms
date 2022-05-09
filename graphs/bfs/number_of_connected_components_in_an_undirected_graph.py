class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj, visited, queue, count = {}, set(), deque(), 0

        for i in range(n):
            adj[i] = []

        # Building out our adjaceny list
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        for vertex in range(n):
            if vertex in visited:
                continue

            queue.append(vertex)

            # Using BFS to visit each node
            while queue:
                curr_node = queue.popleft()

                if curr_node in visited:
                    continue

                visited.add(curr_node)

                for nei in adj[curr_node]:
                    queue.append(nei)

            count += 1

        return count

# Time complexity: O(V + E) because we are traversing
# each node once.

# Space Complexity: O(V + E) to build out the adjaceny list.

# Solution: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/400707/Simple-DFS-and-BFS-Python-solutions-using-a-dictionary