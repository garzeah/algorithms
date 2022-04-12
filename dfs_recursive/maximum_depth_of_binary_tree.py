# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We have traveled every possible node
        if root is None:
            return 0

        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)

        # Finds the max of both sides
        return max(left_depth, right_depth) + 1

# Time Complexity: O(n)
# Space Complexity: O(n)