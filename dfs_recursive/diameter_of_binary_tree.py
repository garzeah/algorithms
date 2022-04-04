# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.tree_diameter = 0
        self.dfs(root)
        return self.tree_diameter

    def dfs(self, curr_node):
        if curr_node is None:
            return 0

        left_depth = self.dfs(curr_node.left)
        right_depth = self.dfs(curr_node.right)

        # Diameter at the current node will be equal to the
        # height of left subtree + the height of right sub-trees
        diameter = left_depth + right_depth

        # Update the global tree diameter
        self.tree_diameter = max(self.tree_diameter, diameter)

        # Height of the current node will be equal to the maximum of the
        # heights of left or right subtrees plus '1' for the current node
        return max(left_depth, right_depth) + 1

# Time Complexity: O(n) bc we traverse through each node once

# Space Complexity: O(n), space is used to store the recursion stack.
# This will happen if the given tree is a Linked List