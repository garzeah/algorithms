# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        # If the value of our root is greater than both p and q it can't be the LCA
        if root.val > p.val and root.val > q.val:
            # Want a smaller value since it is a BST
            return self.lowestCommonAncestor(root.left, p, q)
        # If the value of our root is less than both p and q it can't be the LCA
        elif root.val < p.val and root.val < q.val:
            # Want a bigger value since it is a BST
            return self.lowestCommonAncestor(root.right, p, q)
        # Means it is equal to or between p and q
        else:
            return root

# Time Complexity: O(n)
# Space Complexity: O(n)