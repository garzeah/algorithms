# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return

        # If we find either p or q then return the root
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both children return a node that means both
        # p and q were found so the parent is the LCA
        if left and right:
            return root

        # Only left or right returned a node meaning p and q are only on one side
        # of the tree (left or right). If both p and q are on one side then that
        # means whichever is encountered first is the LCA
        return left or right

# Time Complexity: O(n)
# Space Complexity: O(n)