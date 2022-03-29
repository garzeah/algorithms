# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, curr_node, depth):
        # We have traveled every possible node
        if curr_node is None:
            return depth

        # Finds the max of both sides of the tree
        return max(
            self.dfs(curr_node.left, depth + 1),
            self.dfs(curr_node.right, depth + 1)
        )

# Time Complexity: O(n)
# Space Complexity: O(n)