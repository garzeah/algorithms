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

        # A valid tree means that...
        #   - And there are no loops
        #   - All nodes are connected
        visited = set()
        queue = deque([[None, 0]])

        while queue:
            prev, curr = queue.popleft()

            # Checking if we have a cycle
            if curr in visited:
                return False

            visited.add(curr)

            for nei in adj[curr]:
                # If our neighbor is equal to the previous vertex then we want to
                # continue since it is a false positive because it is marked as
                # visited already so we want to check the next neighbor
                if nei != prev:
                    queue.append([curr, nei])

        # Checking if all nodes are connected
        return len(visited) == n

# Time Complexity: O(V + E) because we visit each node once.

# Space Complexity: O(V + E) because we make an adjaceny list of every node and edge.

# Solution: https://leetcode.com/problems/graph-valid-tree/discuss/1543198/Fast-Python-BFS-with-some-notes-on-intuition