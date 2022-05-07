class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = {}

        # Setting up our adjacent list
        for i in range(n):
            adj[i] = []

        # Adding our connections in our adjaceny list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        queue, visited = deque([0]), set({0})

        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == n

# Time Complexity: O(V + E) because we visit each node once.

# Space Complexity: O(V + E) because we make an adjaceny list of every node and edge.

# Solution: https://leetcode.com/problems/graph-valid-tree/discuss/319570/Python3-clear-UnionFindBFSDFS-(iterative%2Brecursive)-solutions

