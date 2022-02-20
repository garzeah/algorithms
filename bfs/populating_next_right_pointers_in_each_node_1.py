"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return

        queue = deque()
        queue.append(root)

        while queue:
            prev_node = None
            level_size = len(queue)

            # Connect all nodes of this level
            for _ in range(level_size):
                curr_node = queue.popleft()

                if prev_node:
                    prev_node.next = curr_node

                prev_node = curr_node

                # Insert the children of current node in the queue
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return root

# Time Complexity: O(n)
# Space Complexity: O(n)