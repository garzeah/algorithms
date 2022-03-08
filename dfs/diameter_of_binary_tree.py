# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tree_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculate_height(root)
        return self.tree_diameter

    def calculate_height(self, curr_node):
        if curr_node is None:
            return 0

        left_tree_height = self.calculate_height(curr_node.left)
        right_tree_height = self.calculate_height(curr_node.right)

        # If the current node doesn't have a left or right subtree, we can't have
        # a path passing through it, since we need a leaf node on each side
        if left_tree_height is not None and right_tree_height is not None:

            # Diameter at the current node will be equal to the
            # height of left subtree + the height of right sub-trees
            diameter = left_tree_height + right_tree_height

            # Update the global tree diameter
            self.tree_diameter = max(self.tree_diameter, diameter)

        # Height of the current node will be equal to the maximum of the
        # heights of left or right subtrees plus '1' for the current node
        return max(left_tree_height, right_tree_height) + 1

# Time Complexity: O(n) bc we traverse through each node once

# Space Complexity: O(n), space is used to store the recursion stack.
# This will happen if the given tree is a Linked List