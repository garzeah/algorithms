# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.dfs(root.left, root.right)

    def dfs(self, root1, root2):
        # Path ended at the same node
        if root1 is None and root2 is None:
            return True

        # Path did not end at the same node
        if root1 is None or root2 is None:
            return False

        # Doesn't have the same values
        if root1.val != root2.val:
            return False

        # Since we are checking for mirrored values
        return self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)

# Time Complexity: O(n)
# Space Complexity: O(n)