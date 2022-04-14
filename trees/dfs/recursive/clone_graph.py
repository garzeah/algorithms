"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return

        # Used to keep track of new cloned nodes
        # by mapping old node to new node
        old_to_new = {}
        return self.dfs(node, old_to_new)

    def dfs(self, curr_node, old_to_new):
        if curr_node in old_to_new:
            return old_to_new[curr_node]

        # Updating the nodes we have cloned so far
        copy = Node(curr_node.val)
        old_to_new[curr_node] = copy

        # Making copies of the neighbors
        for neighbor in curr_node.neighbors:
            copy.neighbors.append(self.dfs(neighbor, old_to_new))

        return copy

# Time Complexity: O(V) + O(E)
# Space Complexity: O(V) + O(E)
