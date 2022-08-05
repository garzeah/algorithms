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
            prev = None

            # Connect all nodes of this level
            for _ in range(len(queue)):
                curr = queue.popleft()

                if prev:
                    prev.next = curr

                prev = curr

                # Insert the children of current node in the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return root

# Time Complexity: O(n)
# Space Complexity: O(n)