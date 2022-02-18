# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque()
        queue.append(root)
        min_tree_depth = 0

        while queue:
            min_tree_depth += 1
            level_size = len(queue)

            for _ in range(level_size):
                curr_node = queue.popleft()

                # Check if this is a leaf node
                if not curr_node.left and not curr_node.right:
                    return min_tree_depth

                # Insert the children of current node in the queue
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

# Time Complexity: O(n)
# Space Complexity: O(n)