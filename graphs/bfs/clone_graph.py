class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        old_to_new, visited, queue = {}, set(), deque([node])

        while queue:
            curr_node = queue.popleft()

            if curr_node in visited:
                continue

            visited.add(curr_node)

            # Creating a clone
            if curr_node not in old_to_new:
                old_to_new[curr_node] = Node(curr_node.val)

            # Appending all the corresponding neighbors
            for nei in curr_node.neighbors:
                # Creating a clone for the neighbors
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)

                # Adding the neighbors to our cloned node
                old_to_new[curr_node].neighbors.append(old_to_new[nei])
                queue.append(nei)

        return old_to_new[node]

# Time Complexity: O(V) + O(E)
# Space Complexity: O(V) + O(E)
# Solution: https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).