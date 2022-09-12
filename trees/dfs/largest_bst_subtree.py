# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.size = 0
        self.dfs(root)
        return self.size

    def dfs(self, root):
        if root is None:
            # When we hit our base case we want to keep track of...
            # 1) Is it a bst?
            # 2) Is the left child < root
            # 3) Is the right child > root
            # 4) Size of the sub-tree
            # Want to keep track of min and max so we can use the left_max and right_min
            # to determine whether the subtree is a valid BST at our current root. We
            # will also use the left_min and right_max to calculate to calculate the
            # the values we need when comparing the root to left_max and right_min
            return [True, 0, float('inf'), float('-inf')]

        left_is_bst, left_size, left_min, left_max = self.dfs(root.left)
        right_is_bst, right_size, right_min, right_max = self.dfs(root.right)

        # If we have a binary search tree...
        if (
            left_is_bst and
            right_is_bst and
            root.val > left_max and
            root.val < right_min
        ):
            # Want to record left_min and right_max to compare against root.val
            left_min = min(left_min, root.val)
            right_max = max(right_max, root.val)

            # Calculate the max length
            local_size = left_size + right_size + 1
            self.size = max(self.size, local_size)

            # Continue building off of it
            return [True, local_size, left_min, right_max]
        else:
            # We don't have a valid BST so just return false
            return [False, 0, float('inf'), float('-inf')]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution: https://www.youtube.com/watch?v=t3kHAoRT5iQ