"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Using obj. to keeping track of whether
        # a node has been cloned or not
        return self.dfs(node, {})

    def dfs(self, curr_node, old_to_new):
        if curr_node is None:
            return

        # If it already has been cloned, return new node
        if curr_node in old_to_new:
            return old_to_new[curr_node]

        # Otherwise, create a clone of the node
        clone = Node(curr_node.val)
        old_to_new[curr_node] = clone

        # Traversing through each node and adding the
        # neighbors it has in the original node
        for nei in curr_node.neighbors:
            clone.neighbors.append(self.dfs(nei, old_to_new))

        return clone

# Time Complexity: O(V) + O(E)
# Space Complexity: O(V) + O(E)
# Solution: https://www.youtube.com/watch?v=mQeF6bN8hMk