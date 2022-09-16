# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root

        result = []
        queue = deque([root])

        while queue:
            # Appending the last value of the queue
            # to get the right side view
            result.append(queue[-1].val)

            for _ in range(len(queue)):
                curr_node = queue.popleft()

                # Insert the children of current node in the queue
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)