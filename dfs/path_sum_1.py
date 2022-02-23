# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        # If the current node is a leaf and its value is equal to the sum, we've found a path
        if root.val == targetSum and root.left is None and root.right is None:
            return True

        # Recursively call to traverse the left and right sub-tree
        # Return true if any of the two recursive call return true
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# Time Complexity: O(n) where n is the total number of nodes on the tree

# Space Complexity: O(n) where this space will be used by the recursion stack. The worst case is when the given
# tree is a linked list (every node has one child)