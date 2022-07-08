class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        queue, visited = deque([node]), set()
        old_to_new = {}

        while queue:
            curr = queue.popleft()

            if curr in visited:
                continue

            visited.add(curr)

            # If curr hasn't been cloned yet then create one
            if curr not in old_to_new:
                old_to_new[curr] = Node(curr.val)

            # Visiting corresponding neighbors
            for nei in curr.neighbors:
                clone = old_to_new[curr]

                # If the neighbor hasn't been cloned yet, create one
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)

                # Want to add the corresponding neighbors to the cloned node
                clone.neighbors.append(old_to_new[nei])
                queue.append(nei) # BFS

        return old_to_new[node]

# Time Complexity: O(V) + O(E)
# Space Complexity: O(V) + O(E)
# Solution: https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).