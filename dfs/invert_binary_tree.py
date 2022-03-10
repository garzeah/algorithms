# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # General case:
            # Invert child node of current root
            root.left, root.right = root.right, root.left

            # Invert subtree with DFS
            if root.left:
                self.invertTree( root.left )

            if root.right:
                self.invertTree( root.right )

            return root
        else:
            # Base case:
            # Empty tree
            return None

# Time Complexity: O(n)
# Space Complexity: O(n)
