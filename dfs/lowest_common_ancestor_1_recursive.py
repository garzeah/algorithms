# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case
        if root is None:
            return

        # Recursive Cases
        # We want a smaller root that is between p and q
        # so we traverse left side since it's a BST
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        # We want a bigger root that is between p and q
        # so we traverse the right side since it's a BST
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)

        # Otherwise we have our LCA
        return root

# Time Complexity: O(n)
# Space Complexity: O(n)