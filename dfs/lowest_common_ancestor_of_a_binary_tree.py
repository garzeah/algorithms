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

        # Either one of the chidren returned a node, meaning either
        # p or q was found on the left or right branch.
        # Example: assuming 'p' found in the left child and right child returned
        # 'None'. This means 'q' is somewhere below the node where 'p' was found.
        # We dont need to search all the way because in such scenarios,
        # the node where 'p' found is the LCA
        return left or right

# Time Complexity: O(n)
# Space Complexity: O(n)